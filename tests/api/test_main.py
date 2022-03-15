"""Main tests"""
from unittest.mock import patch

from fastapi.testclient import TestClient

from app import settings


def test_address_balance(client: TestClient) -> None:
    """Test to read balance"""
    return_value_erc20 = "1000.00"
    return_value_nft = 2

    # Invalid address
    response = client.get(
        f"{settings.API_V1_STR}/wallet/balance/0x00/",
    )
    assert response.status_code == 400

    # Valid address
    with patch("app.routers.v1.wallet.get_acr_balance", return_value=return_value_erc20), patch(
        "app.routers.v1.wallet.get_nft_balance", return_value=return_value_nft
    ):
        address = "0xCBCAd2A0abaB2aC7EA7D71113a779218C7052cA4"
        response = client.get(
            f"{settings.API_V1_STR}/wallet/balance/{address}/",
        )
        assert response.status_code == 200
        content = response.json()
        assert content["erc20"] == return_value_erc20
        assert content["erc721"] == return_value_nft
