# from collections.abc import AsyncGenerator
#
# import pytest
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
#
# #from migrations.env import target_metadata
# #from sqlalchemy.orm import DeclarativeBase
# #from migrations.env import target_metadata
# from my_app_new.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME_TEST
# from my_app_new.database import Base
# from my_app_new.dependencies import get_async_session
# from my_app_new.main import app
#
# # from my_app_new.operations.models import Author, Book # noqa
# # from my_app_new.auth.models import User # noqa
#
#
# DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"
#
#
# engine_test = create_async_engine(DATABASE_URL_TEST)
# async_session_maker_t = async_sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False) # bind=engine_test)
#
# #Base = DeclarativeBase()
#
# #target_metadata.bind = engine_test  # возможно метаданные заново придется делать
# metadata = Base.metadata
# metadata.bind = engine_test
#
#
#
#
#
# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker_t() as session:
#         yield session
#
#
# app.dependency_overrides[get_async_session] = override_get_async_session

