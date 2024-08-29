# tests/test_fastapi.py

from fastapi.testclient import TestClient
from apiannegit import app  # Replace 'your_app_module_name' with the actual name of your Python file

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, stranger"}

def test_get_name():
    response = client.get("/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John"}

    response = client.get("/Jane")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Jane"}
