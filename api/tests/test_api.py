import sys
import os
import pytest
import sqlite3
from api.api import app , db_connection

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Forcer le chemin courant vers le répertoire contenant books.sqlite
os.chdir(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    if response.json:
        assert all('id' in book and 'author' in book and 'language' in book and 'title' in book for book in response.json)

def test_post_book(client):
    # Données fictives pour le test
    data = {
        'author': 'Test Author',
        'language': 'Test Language',
        'title': 'Test Title'
    }
    response = client.post('/books', data=data)
    assert response.status_code == 200 or response.status_code == 201