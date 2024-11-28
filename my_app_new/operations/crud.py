
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from sqlalchemy import select
from my_app_new.operations import models, schemas

#
# def get_author(db: Session, author_id: int):
#     return db.query(models.Author).filter(models.Author.id == author_id).first()
#
#
# def get_author_by_author_name(db: Session, author_name: str):
#     return db.query(models.Author).filter(models.Author.author_name == author_name).first()
#
#
# def get_authors(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Author).offset(skip).limit(limit).all()
#
#
# def create_author(db: Session, author: schemas.AuthorCreate):
#
#     db_author = models.Author(author_name=author.author_name)
#     db.add(db_author)
#     db.commit()
#     db.refresh(db_author)
#     return db_author
#

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 100):
    #return db.select(models.Book).offset(skip).limit(limit).all()
    query = select(models.Book).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
    # a = result.scalars().all()
    # a = list(a)
    # return a

#
# def create_book_author(db: Session, book: schemas.BookCreate, author_id: int):
#     db_book = models.Book(**book.dict(), author_id=author_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book
