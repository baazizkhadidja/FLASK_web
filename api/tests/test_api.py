import pytest
from api import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_single_book(client):
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "title" in data

def test_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404