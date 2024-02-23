"""Test for the timestamp endpoint."""

import pytest
from datetime import datetime


def test_timestamp_endpoint(client):
    response = client.get("/timestamp")
    assert response.status_code == 200
    timestamp = response.json().get("timestamp")
    # Ensure the timestamp is in ISO format and recent
    assert datetime.fromisoformat(timestamp)
    assert (datetime.utcnow() - datetime.fromisoformat(timestamp)).seconds < 5
