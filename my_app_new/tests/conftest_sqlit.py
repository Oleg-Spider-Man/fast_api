# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from my_app_new.database import Base
# from my_app_new.dependencies import get_async_session
# from my_app_new.main import app
# from my_app_new.operations.models import Author, Book # noqa
# from my_app_new.auth.models import User # noqa
#
# SQL_DB_URL = f"sqlite:///.bd_test"
# engine_test = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
#
# metadata = Base.metadata
# metadata.bind = engine_test
#
#
# def override_get_async_session():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# app.dependency_overrides[get_async_session] = override_get_async_session
