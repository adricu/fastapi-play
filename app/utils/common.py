"""Common utils"""
import logging
from decimal import Decimal

from web3 import Web3

LOGGER = logging.getLogger(__name__)

COMMON_ERC20_TOKEN_DECIMALS = 18


def decimal_to_wei(erc20, token_decimals=COMMON_ERC20_TOKEN_DECIMALS):  # pragma: no cover
    """Converts an ERC20/Ether to wei"""
    return int(Decimal(str(erc20)) * Decimal(f"1e{token_decimals}"))


def wei_to_decimal(wei, token_decimals=COMMON_ERC20_TOKEN_DECIMALS):  # pragma: no cover
    """Converts a wei to ERC20/Ether"""
    return Decimal(str(wei)) * Decimal(f"1e-{token_decimals}")


def validate_address(value):
    """Ensures that a wallet address is valid"""
    return Web3.isChecksumAddress(value)
