"""Pytest conftest"""
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.controller import create_api
from app.utils.common import Environment, load_config
from app.utils.logging.config import configure_logging


@pytest.fixture(scope="module")
def client() -> Generator:
    """Test client for api requests"""
    config = load_config(Environment.TEST)
    configure_logging(config)
    api = create_api(config)
    with TestClient(api) as test_client:
        yield test_client
