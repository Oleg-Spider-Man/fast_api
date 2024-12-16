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
async def test_get_auth(aclient):
    login_data = {
        "username": "user@example.com",
        "password": "string"
    }
    response = await aclient.post("/auth/jwt/login", data=login_data)
    assert response.status_code == 204 # 200

    # Получаем куки из ответа
    cookies = response.cookies

    # Проверяем наличие токена в куки
    token_cookie = cookies.get('cookie_fast_api_new')
    assert token_cookie is not None
    # разобраться как куки получить в глобальную переменную и использовать в других тестах
    global_access_token = token_cookie
    pytest.global_vars['access_token'] = global_access_token


