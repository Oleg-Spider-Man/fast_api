import asyncio
import httpx
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from my_app_new.config import DB_USER, DB_HOST, DB_PORT, DB_NAME_TEST, DB_PASS
from my_app_new.database import Base
from my_app_new.dependencies import get_async_session
from my_app_new.main import app


DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL_TEST, echo=True)

TestSessionLocal = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)#sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)

metadata = Base.metadata


async def override_get_async_session():
    async with TestSessionLocal() as session:
        yield session
        # Откатываем транзакции после теста
        await session.rollback()

app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(scope='session')  # ,  autouse=True)
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# @n-ellocoPytest-asyncio v0.24 поддерживает запуск тестов в различных циклах событий.
# Для каждого уровня набора тестов (сеанс, пакет, модуль, класс, функция) есть цикл.
# Однако pytest-asyncio ошибочно предполагает, что область действия асинхронной фикстуры совпадает с областью
# действия цикла событий, в котором выполняется фикстура. Это по сути делает невозможным наличие фикстуры
# с областью действия сеанса, которая выполняется в том же цикле, что и тест с областью действия функции. См. #706 .


@pytest.fixture(scope="function", autouse=True)
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

