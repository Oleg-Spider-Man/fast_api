import asyncio
import httpx
import pytest
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from my_app_new.background_tasks.celery_task import celery_app
from my_app_new.config import DB_USER, DB_HOST, DB_PORT, DB_NAME_TEST, DB_PASS
from my_app_new.database import Base
from my_app_new.dependencies import get_async_session
from my_app_new.main import app


DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=pool.NullPool, echo=True)
# NullPool для тестов можно, для продакшена нельзя.
TestSessionLocal = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)

metadata = Base.metadata


async def override_get_async_session():
    async with TestSessionLocal() as session:
        yield session
        # Откатываем транзакции после теста
        await session.rollback()


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def db_session():
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
async def aclient():
    async with httpx.AsyncClient(app=app, base_url="http://test") as aclient:
        yield aclient


@pytest.fixture(scope="function")
def celery_worker():
    # Используем celery синхронно в тестах без ожидания брокера сообщений или отдельного воркера
    # для асинхронного теста эту фисктуру можно убрать, но тогда нужно включить celery и redis
    celery_app.conf.update(task_always_eager=True)
    yield celery_app
