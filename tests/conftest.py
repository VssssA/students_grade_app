import asyncio
import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def test_app():
    return TestClient(app)


