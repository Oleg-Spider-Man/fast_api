from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    description: str
    genre: str
    price: int


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True


class AuthorCreate(BaseModel):
    author_name: str


class AuthorRead(AuthorCreate):
    id: int
    #books: list[Book] = []

    class Config:
        orm_mode = True
