from typing import List

from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    description: str
    genre: str
    price: int
    author_id: int


# class ResponseBook(BaseModel):
#     books: List[BookCreate]


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True


class AuthorCreate(BaseModel):
    author_name: str


class AuthorRead(AuthorCreate):
    id: int

    class Config:
        orm_mode = True
