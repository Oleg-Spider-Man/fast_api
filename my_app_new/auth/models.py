from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer
from my_app_new.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)