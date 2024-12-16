import pytest


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
