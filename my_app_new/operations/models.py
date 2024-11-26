from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from my_app_new.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    author_name = Column(String(20))
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), index=True)
    description = Column(String)
    genre = Column(String(50))
    price = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship("Author", back_populates="books")
