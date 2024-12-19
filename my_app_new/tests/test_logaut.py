import pytest


@pytest.mark.asyncio
async def test_logout(aclient):
    response = await aclient.post("/auth/jwt/logout")
    aclient.cookies.clear()
    assert aclient.cookies.get("cookie_fast_api_new") is None
    assert response.status_code == 204
