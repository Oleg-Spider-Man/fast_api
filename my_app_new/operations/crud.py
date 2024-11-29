
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from my_app_new.operations import models, schemas

#
# def get_author(db: AsyncSession, author_id: int):
#     return db.query(models.Author).filter(models.Author.id == author_id).first()


async def get_author_by_author_name(db: AsyncSession, author_name: str):
    query = select(models.Author).filter(models.Author.author_name == author_name)
    result = await db.execute(query)
    return result.scalar()
# return db.query(models.Author).filter(models.Author.author_name == author_name).first() было так


async def get_authors(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Author).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def create_author(db: AsyncSession, author: schemas.AuthorCreate):

    db_author = models.Author(author_name=author.author_name)
    db.add(db_author)
    await db.commit()
    return db_author


async def get_books(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Book).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


#
# def create_book_author(db: AsyncSession, book: schemas.BookCreate, author_id: int):
#     db_book = models.Book(**book.dict(), author_id=author_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book
