import httpx
import pytest
from fastapi.testclient import TestClient
from my_app_new.main import app
from my_app_new.operations import crud
#from my_app_new.auth.schemas import AuthorCreate

client = TestClient(app)


# @pytest.mark.asyncio
# async def test_create_author():#db_session):
#     # Переопределяем зависимость get_async_session на нашу фикстуру db_session
#     payload = {"author_name": "Jane Doe"}
#
#     # Выполняем запрос для создания автора
#     response = client.post(
#         "/authors/", json=payload #headers={"Authorization": "Bearer <your-jwt-token>"}
#     )
#
#     assert response.status_code == 200
#     assert response.json()['author_name'] == "Jane Doe"

    # # Проверяем, что автор был добавлен в базу данных
    # db_author = await crud.get_author_by_author_name(db_session, "Jane Doe")
    # assert db_author is not None
    # assert db_author.author_name == "Jane Doe"


@pytest.mark.asyncio
async def test_create_author():
    payload = {"author_name": "Jane Doe"}

    # Используем асинхронный клиент httpx.AsyncClient
    async with httpx.AsyncClient(app=app, base_url="http://test") as aclient:
        response = await aclient.post("/authors/", json=payload)

    assert response.status_code == 200
    assert response.json()['author_name'] == "Jane Doe"


@pytest.mark.asyncio
async def test_read_books():

    # Используем асинхронный клиент httpx.AsyncClient
    async with httpx.AsyncClient(app=app, base_url="http://test") as aclient:
        response = await aclient.get('/books/')

    assert response.status_code == 200

