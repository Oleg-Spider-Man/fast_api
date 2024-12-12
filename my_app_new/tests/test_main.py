import pytest
from fastapi.testclient import TestClient
from my_app_new.main import app
client = TestClient(app)


@pytest.mark.asyncio
async def test_create_author(aclient):
    payload = {"author_name": "Jane Doe"}
    response = await aclient.post("/authors/", json=payload)
    assert response.status_code == 200
    assert response.json()['author_name'] == "Jane Doe"


@pytest.mark.asyncio
async def test_read_books(aclient):
    response = await aclient.get('/books/')
    assert response.status_code == 200

