# import pytest
# from fastapi.testclient import TestClient
# from httpx import AsyncClient, ASGITransport
#
# from my_app_new.main import app
#
# client = TestClient(app)
#
#
# # @pytest.mark.anyio
# # async def test_root():
# #     async with AsyncClient(
# #         transport=ASGITransport(app=app), base_url="http://test"
# #     ) as ac:
# #         response = await ac.get("/books/")
# #     assert response.status_code == 200
#
# @pytest.mark.asyncio
# async def test_read_books():
#     response = client.get('/books/')
#     assert response.status_code == 200
#
#
# def test_r():
#     assert 200 == 200
