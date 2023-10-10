"""Main tests"""
from decimal import Decimal
from functools import partial
from unittest.mock import patch

from fastapi import status
from fastapi.testclient import TestClient
from httpx import BasicAuth

ADDRESS_BALANCE_ENDPOINT = partial(
    "/v1/wallet/balance/{address}".format  # pylint: disable=consider-using-f-string
)


def test_address_balance(
    client: TestClient,
    public_auth: BasicAuth,
    secure_auth: BasicAuth,
) -> None:
    """Test to read balance"""
    return_value_erc20 = Decimal("1000.00")
    return_value_nft = 2

    # Not auth or wrong
    response = client.get(ADDRESS_BALANCE_ENDPOINT(address="0x00"))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.get(
        ADDRESS_BALANCE_ENDPOINT(address="0x00"), auth=BasicAuth("a", "b")
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Invalid address
    response = client.get(ADDRESS_BALANCE_ENDPOINT(address="0x00"), auth=public_auth)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "is not a valid address" in response.json()["detail"]

    # Valid address
    with patch(
        "app.routers.v1.wallet.get_acr_balance", return_value=return_value_erc20
    ), patch("app.routers.v1.wallet.get_nft_balance", return_value=return_value_nft):
        address = "0xCBCAd2A0abaB2aC7EA7D71113a779218C7052cA4"
        response = client.get(
            ADDRESS_BALANCE_ENDPOINT(address=address), auth=public_auth
        )
        assert response.status_code == status.HTTP_200_OK
        content = response.json()
        assert content["erc20"] == str(return_value_erc20)
        assert content["erc721"] == return_value_nft

        response = client.get(
            ADDRESS_BALANCE_ENDPOINT(address=address), auth=secure_auth
        )
        assert response.status_code == status.HTTP_200_OK
        content = response.json()
        assert content["erc20"] == str(return_value_erc20)
        assert content["erc721"] == return_value_nft


def test_exception_handlers(client: TestClient, public_auth: BasicAuth) -> None:
    """Test to read balance"""
    address = "0xCBCAd2A0abaB2aC7EA7D71113a779218C7052cA4"
    with patch("app.routers.v1.wallet.validate_address", side_effect=Exception):
        response = client.get(
            ADDRESS_BALANCE_ENDPOINT(address=address), auth=public_auth
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert "error_message" in response.json()
