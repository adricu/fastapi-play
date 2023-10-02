"""Test root api endpoints."""
from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    """Test health endpoint"""
    response = client.get("/healthz")
    assert response.status_code == 200
