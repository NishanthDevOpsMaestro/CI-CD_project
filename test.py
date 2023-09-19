import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Buddy!" in response.data

def test_home_page_content(client):
    response = client.get('/')
    assert b"Welcome to our App" in response.data

def test_about_page_content(client):
    response = client.get('/about')
    assert b"About Us" in response.data

def test_contact_page_content(client):
    response = client.get('/contact')
    assert b"Contact Us" in response.data
