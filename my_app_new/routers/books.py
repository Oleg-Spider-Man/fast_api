from fastapi import APIRouter, Depends
from my_app_new import schemas
from my_app_new.operations import crud
from my_app_new.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get("/", response_model=list[schemas.Item])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books
