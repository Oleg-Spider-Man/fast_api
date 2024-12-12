from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from my_app_new.auth.user_obj import current_user
from my_app_new.dependencies import get_async_session
from my_app_new.operations import crud, schemas


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)

#, dependencies=[Depends(current_user)]
@router.post("/", response_model=schemas.AuthorRead)
async def create_author(author: schemas.AuthorCreate, db: AsyncSession = Depends(get_async_session)):
    db_author = await crud.get_author_by_author_name(db, author_name=author.author_name)
    if db_author:
        raise HTTPException(status_code=400, detail="Author name already registered")
    return await crud.create_author(db=db, author=author)


@router.get("/", dependencies=[Depends(current_user)], response_model=list[schemas.AuthorRead])
async def read_authors(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    authors = await crud.get_authors(db=db, skip=skip, limit=limit)
    return authors


@router.get("/{author_id}", dependencies=[Depends(current_user)], response_model=schemas.AuthorRead)
async def read_author(author_id: int, db: AsyncSession = Depends(get_async_session)):
    db_author = await crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.post("/{author_id}/books/", dependencies=[Depends(current_user)], response_model=schemas.Book)
async def create_book_for_author(
    author_id: int, book: schemas.BookCreate, db: AsyncSession = Depends(get_async_session)
):
    db_author = await crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return await crud.create_book_author(db=db, book=book, author_id=author_id)
