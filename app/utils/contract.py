"""Contract related calls"""
from decimal import Decimal
import logging
import os

from envyaml import EnvYAML
from web3 import Web3
from web3.contract.contract import Contract
from web3.types import BlockIdentifier

from app.utils.common import BASE_DIR

LOGGER = logging.getLogger(__name__)


COMMON_ERC20_TOKEN_DECIMALS = 18
ABI_PATH = os.path.join(BASE_DIR, "abi")
ACR_TOKEN_DECIMALS = 18


def decimal_to_wei(
    decimal_amount: Decimal, token_decimals: int = COMMON_ERC20_TOKEN_DECIMALS
) -> int:
    """Converts an ERC20/Ether to wei"""
    return int(decimal_amount * Decimal(f"1e{token_decimals}"))


def wei_to_decimal(
    wei: int, token_decimals: int = COMMON_ERC20_TOKEN_DECIMALS
) -> Decimal:
    """Converts a wei to ERC20/Ether."""
    return Decimal(str(wei)) * Decimal(f"1e-{token_decimals}")


def validate_address(address: str) -> bool:
    """Ensures that a wallet address is valid"""
    return Web3.is_checksum_address(address)


def get_web3_client(blockchain_config: EnvYAML) -> Web3:
    """Returns initialized web3 client."""
    infura_config = blockchain_config["node"]["infura"]
    infura_network = infura_config["network"]
    infura_project_id = infura_config["project_id"]
    if infura_network and infura_project_id:
        infura_project_secret = infura_config["project_secret"]
        rpc_url = f"https://:{infura_project_secret}@{infura_network}.infura.io/v3/{infura_project_id}"
    else:
        rpc_url = blockchain_config["node"]["rpc_url"]
    assert rpc_url
    return Web3(
        Web3.HTTPProvider(
            rpc_url,
        )
    )


def get_erc20_contract(blockchain_config: EnvYAML) -> Contract:
    """Returns ERC20 contract."""
    with open(
        os.path.join(ABI_PATH, "ACRToken.abi"), "r", encoding="UTF-8"
    ) as contract_abi_file:
        erc20_contract_abi = contract_abi_file.read()
    contract: Contract = get_web3_client(blockchain_config).eth.contract(
        address=blockchain_config["contracts"]["erc20"],
        abi=erc20_contract_abi,
    )
    return contract


def get_nft_contract(blockchain_config: EnvYAML) -> Contract:
    """Returns NTF contract."""
    with open(
        os.path.join(ABI_PATH, "ACRNFT.abi"), "r", encoding="UTF-8"
    ) as contract_abi_file:
        nft_contract_abi = contract_abi_file.read()
    contract: Contract = get_web3_client(blockchain_config).eth.contract(
        address=blockchain_config["contracts"]["nft"],
        abi=nft_contract_abi,
    )
    return contract


def get_acr_balance(
    blockchain_config: EnvYAML,
    address: str,
    block_identifier: BlockIdentifier = "latest",
) -> Decimal:
    """Returns the ACR token balance of a wallet address"""
    return wei_to_decimal(
        get_erc20_contract(blockchain_config)
        .get_function_by_name("balanceOf")(address)
        .call(**{"block_identifier": block_identifier}),
        ACR_TOKEN_DECIMALS,
    )


def get_nft_balance(
    blockchain_config: EnvYAML,
    address: str,
    block_identifier: BlockIdentifier = "latest",
) -> int:
    """Returns the ACR NFT balance of a wallet address"""
    return int(
        get_nft_contract(blockchain_config)
        .get_function_by_name("balanceOf")(address)
        .call(**{"block_identifier": block_identifier})
    )


def get_current_block_number(blockchain_config: EnvYAML) -> int:
    """Returns the current block number"""
    return get_web3_client(blockchain_config).eth.block_number


def get_latest_block_timestamp(blockchain_config: EnvYAML) -> int:
    """Returns the timestamp of the latest block"""
    last_block = get_web3_client(blockchain_config).eth.get_block("latest")
    return last_block["timestamp"]


def get_net_version(blockchain_config: EnvYAML) -> str:
    """Returns net version"""
    return get_web3_client(blockchain_config).net.version
