from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_unknown_route_returns_404():
    response = client.get("/random-resource")
    assert response.status_code == 404
