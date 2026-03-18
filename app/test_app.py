import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200

def test_data(client):
    r = client.get('/data')
    assert r.status_code == 200
