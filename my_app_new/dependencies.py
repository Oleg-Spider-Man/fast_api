from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from my_app_new.database import async_session_maker


# !!!!!!!!!!!! ПОМЕНЯТЬ ЭТУ СЕССИЮ НА СЕССИЮ ИЗ ДАТАБЕЙС
# def get_db():
#     db = async_session_maker()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
