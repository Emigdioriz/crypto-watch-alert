import pytest
from tests.fixtures.db_fixtures import client

# def test_create_alert_success(client):
# 	payload = {
# 		"symbol": "BTCUSD",
# 		"targetPrice": 50000.00
# 	}
# 	response = client.post("/alerts/", json=payload)
# 	assert response.status_code == 201
# 	data = response.json()
# 	assert "detail" in data
# 	assert "id" in data["detail"]
# 	assert data["detail"]["id"] is not None