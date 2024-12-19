import pytest


@pytest.mark.asyncio
async def test_register(aclient):
    response = await aclient.post("/auth/register", json={
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
     })
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "email": "user@example.com",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False
    }


@pytest.mark.asyncio
async def test_auth(aclient):
    login_data = {
             "username": "user@example.com",
             "password": "string"
         }
    response = await aclient.post("/auth/jwt/login", data=login_data)
    assert response.status_code == 204  # 200
    # Получаем куки из ответа
    cookies = response.cookies
    # Проверяем наличие токена в куки
    token_cookie = cookies.get('cookie_fast_api_new')
    assert token_cookie is not None
    # разобраться как куки получить в глобальную переменную и использовать в других тестах
    aclient.cookies.set("cookie_fast_api_new", token_cookie)


@pytest.mark.asyncio
async def test_create_author(aclient):
    payload = {"author_name": "Jane Doe"}
    response = await aclient.post("/authors/", json=payload)
    assert response.status_code == 200
    assert response.json()['author_name'] == "Jane Doe"


@pytest.mark.asyncio
async def test_read_authors(aclient):
    response = await aclient.get("/authors/")
    assert response.status_code == 200
    assert response.json() == [{"author_name": "Jane Doe", "id": 1}]


@pytest.mark.asyncio
async def test_read_author(aclient):
    response = await aclient.get("/authors/1")
    assert response.status_code == 200
    assert response.json() == {"author_name": "Jane Doe", "id": 1}


@pytest.mark.asyncio
async def test_create_book_for_author(aclient):
    response = await aclient.post("/authors/1/books/", json={
     "title": "Богатство",
     "description": "очень интересные события",
     "genre": "роман-эпопея",
     "price": 177
    })
    assert response.status_code == 200
    assert response.json() == {
     "title": "Богатство",
     "description": "очень интересные события",
     "genre": "роман-эпопея",
     "price": 177,
     "id": 1
    }


@pytest.mark.asyncio
async def test_read_books(aclient):
    response = await aclient.get('/books/')
    assert response.status_code == 200
    assert response.json() == [{
     "title": "Богатство",
     "description": "очень интересные события",
     "genre": "роман-эпопея",
     "price": 177,
     "id": 1
    }]
