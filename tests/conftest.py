"""Pytest conftest"""
from envyaml import EnvYAML
from fastapi.testclient import TestClient
from httpx import BasicAuth
import pytest

from app.controller import create_api
from app.utils.common import BlockchainConfig, Environment, get_blockchain_config, load_config


@pytest.fixture()
def config() -> EnvYAML:
    """Config dictionary from test environment"""
    return load_config(Environment.TEST)


@pytest.fixture()
def blockchain_config() -> BlockchainConfig:
    """BlockchainConfig dataclass from test environment"""
    return get_blockchain_config(Environment.TEST)


@pytest.fixture()
def client(config: EnvYAML) -> TestClient:  # pylint: disable=redefined-outer-name
    """Test client for api requests"""

    return TestClient(create_api(config), raise_server_exceptions=False)


@pytest.fixture()
def public_auth(config: EnvYAML) -> BasicAuth:  # pylint: disable=redefined-outer-name
    """Basic auth for public user"""
    return BasicAuth("public", str(config["api"]["auth"]["public_password"]).encode())


@pytest.fixture()
def secure_auth(config: EnvYAML) -> BasicAuth:  # pylint: disable=redefined-outer-name
    """Basic auth for public user"""
    return BasicAuth("secure", str(config["api"]["auth"]["secure_password"]).encode())
