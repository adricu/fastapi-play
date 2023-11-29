"""Common utils."""
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Optional

from envyaml import EnvYAML
from eth_typing import Address

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REQUESTS_TIMEOUT = (3.05, 27)


@dataclass
class InfuraNode:
    network: str
    project_id: str
    project_secret: str


@dataclass(frozen=True)
class Node:
    infura: Optional[InfuraNode]
    rpc_url: str
    username: str
    password: str


@dataclass(frozen=True)
class Contracts:
    erc20: Address
    nft: Address


@dataclass(frozen=True)
class BlockchainConfig:
    is_poa: bool
    node: Node
    contracts: Contracts


class Environment(str, Enum):
    """Enviornment possibilities."""

    LOCAL = "local"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


ENVIRONMENTS = [environment.value for environment in Environment]


@lru_cache
def load_config(environment: Environment) -> EnvYAML:
    """Load and return app confiuration"""
    config_file_path = f"config/{environment}.yaml"
    if not Path(config_file_path).is_file():
        raise ValueError(
            f"Unable to find configuration file: {config_file_path}."
        )  # pragma: no cover
    return EnvYAML(config_file_path)


@lru_cache
def get_blockchain_config(environment: Environment) -> BlockchainConfig:
    config = load_config(environment)
    infura_network = config["blockchain.node.infura.network"]
    infura_project_id = config["blockchain.node.infura.project_id"]
    infura_node = None
    if infura_network and infura_project_id:  # pragma: no cover
        infura_node = InfuraNode(
            network=infura_network,
            project_id=infura_project_id,
            project_secret=config["blockchain.node.infura.project_secret"],
        )
    return BlockchainConfig(
        is_poa=config["blockchain.is_poa"],
        node=Node(
            infura=infura_node,
            rpc_url=config["blockchain.node.rpc_url"],
            username=config["blockchain.node.username"],
            password=config["blockchain.node.username"],
        ),
        contracts=Contracts(
            erc20=config["blockchain.contracts.erc20"],
            nft=config["blockchain.contracts.nft"],
        ),
    )
