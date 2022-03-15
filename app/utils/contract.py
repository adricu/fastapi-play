"""Contract related calls"""
import logging

from app import settings
from app.utils.common import wei_to_decimal

LOGGER = logging.getLogger(__name__)


def get_acr_balance(address, block_identifier="latest"):  # pragma: no cover
    """Returns the ACR token balance of a wallet address"""
    return wei_to_decimal(
        settings.ACR_TOKEN_PROXY_CONTRACT.get_function_by_name("balanceOf")(address).call(
            **{"block_identifier": block_identifier}
        ),
        settings.ACR_TOKEN_DECIMALS,
    )


def get_nft_balance(address, block_identifier="latest"):  # pragma: no cover
    """Returns the ACR NFT balance of a wallet address"""
    return settings.ACR_NFT_CONTRACT.get_function_by_name("balanceOf")(address).call(
        **{"block_identifier": block_identifier}
    )


def get_current_block_number() -> int:  # pragma: no cover
    """Returns the current block number"""
    return settings.W3.eth.blockNumber


def get_latest_block_timestamp():  # pragma: no cover
    """Returns the timestamp of the latest block"""
    return settings.W3.eth.getBlock("latest").timestamp


def get_net_version():  # pragma: no cover
    """Returns net version"""
    return settings.W3.net.version
