import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def activity_data(monkeypatch):
    activities = {
        "Test Activity": {
            "description": "A test activity",
            "schedule": "Mondays at 3 PM",
            "max_participants": 5,
            "participants": ["student@example.com"],
        }
    }
    monkeypatch.setattr(app_module, "activities", activities)
    return activities


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client