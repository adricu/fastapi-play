"""Pytest conftest"""
from fastapi.testclient import TestClient
import pytest

from app.controller import create_api
from app.utils.common import Environment, load_config


@pytest.fixture()
def client() -> TestClient:
    """Test client for api requests"""
    config = load_config(Environment.TEST)
    return TestClient(create_api(config), raise_server_exceptions=False)
