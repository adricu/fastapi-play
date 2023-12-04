"""Test contract utils."""
from decimal import Decimal

import pytest

from app.utils.common import BlockchainConfig
from app.utils.contract import (
    decimal_to_wei,
    get_acr_balance,
    get_current_block_number,
    get_latest_block_timestamp,
    get_net_version,
    get_nft_balance,
    validate_address,
    wei_to_decimal,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (Decimal(1), 1e18),
    ],
)
def test_decimal_to_wei(test_input: Decimal, expected: int) -> None:
    assert decimal_to_wei(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1e18, Decimal(1)),
    ],
)
def test_wei_to_decimal(test_input: int, expected: Decimal) -> None:
    assert wei_to_decimal(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1e18", False),
    ],
)
def test_validate_address(test_input: str, expected: bool) -> None:
    assert validate_address(test_input) == expected


@pytest.mark.parametrize(
    "address,expected_balance",
    [
        ("0x975cBbAE0eaA9A95f0627f686C72D82badE9BF51", 0),
        ("0xeCB2C897B05Ec5456180169851e6b6C309e6D6D4", 0),
        ("0xa6ef37333F73d6Cc1134C0875877911304361625", 0),
        ("0x0Eee93CF3852bC420Aaf912ac0Ff3226E4238638", 0),
    ],
)
def test_get_acr_balance(address: str, expected_balance: int, blockchain_config: BlockchainConfig) -> None:
    assert get_acr_balance(blockchain_config, address) == expected_balance


@pytest.mark.parametrize(
    "address,expected_balance",
    [
        ("0x975cBbAE0eaA9A95f0627f686C72D82badE9BF51", 0),
        ("0xeCB2C897B05Ec5456180169851e6b6C309e6D6D4", 0),
        ("0xa6ef37333F73d6Cc1134C0875877911304361625", 0),
        ("0x0Eee93CF3852bC420Aaf912ac0Ff3226E4238638", 0),
    ],
)
def test_get_nft_balance(address: str, expected_balance: int, blockchain_config: BlockchainConfig) -> None:
    assert get_nft_balance(blockchain_config, address) == expected_balance


def test_get_current_block_number(blockchain_config: BlockchainConfig) -> None:
    assert get_current_block_number(blockchain_config)


def test_get_latest_block_timestamp(blockchain_config: BlockchainConfig) -> None:
    assert get_latest_block_timestamp(blockchain_config)


def test_get_net_version(blockchain_config: BlockchainConfig) -> None:
    assert get_net_version(blockchain_config)
