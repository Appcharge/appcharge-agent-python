import pytest
import json
from unittest.mock import patch, PropertyMock
import os

os.environ["KEY"] = "KEY"
os.environ["APP_SECRET"] = "APP_SECRET"

from app import app, signature_service


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_update_balance(client):
    with patch.object(signature_service, 'check_signature', return_value=True):
        sample_purchase = {
            "appChargePaymentId": 123,
            "purchaseDateAndTimeUtc": "2023-08-17T00:00:00Z",
            "gameId": "game123",
            "playerId": "player456",
            "bundleName": "Starter Pack",
            "bundleId": "bundle789",
            "sku": "sku101",
            "priceInCents": 100,
            "currency": "USD",
            "priceInDollar": 1.00,
            "action": "purchase",
            "actionStatus": "completed",
            "products": ["item1", "item2"],
            "subTotal": 0.9,
            "tax": 0.1
        }

        response = client.post('/updateBalance', json=sample_purchase)
        
    assert response.status_code == 200
    response_data = response.get_json()
    assert "publisherPurchaseId" in response_data
