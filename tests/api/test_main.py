"""Main tests"""
from fastapi.testclient import TestClient

from app import settings


def test_address_balance(client: TestClient) -> None:
    """Test to read balance"""
    address = ""
    response = client.get(
        f"{settings.API_V1_STR}/balance/{address}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["erc20"] == 1
    assert content["erc721"] == 2
