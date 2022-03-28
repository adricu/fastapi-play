"""Pytest conftest"""
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    """Test client for api requests"""
    with TestClient(app) as test_client:
        yield test_client
