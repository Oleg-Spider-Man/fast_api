from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from my_app_new.auth_.user_obj import current_user
from my_app_new.operations import crud, schemas
from my_app_new.dependencies import get_async_session

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(current_user)]
)


@router.get("/", response_model=list[schemas.Book])
async def read_books(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    books = await crud.get_books(db, skip=skip, limit=limit)
    return books
