import pytest
from unittest.mock import patch, Mock, patch
import os

os.environ["KEY"] = "KEY"
os.environ["APP_SECRET"] = "APP_SECRET"

from app import app, signature_service
from controllers.auth.models import AuthenticationRequest
from controllers.auth.methods.facebook import facebook_login


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_authenticate_player_valid_facebook(client):
    with patch.object(signature_service, 'check_signature', return_value=True):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'data': {
                'is_valid': True,
                'user_id': '12345'
            }
        }

        with patch('controllers.auth.methods.facebook.requests.get', return_value=mock_response):
            response = client.post('/auth', json={
                'authMethod': 'facebook',
                'token': 'test_token',
                'date': '2021-08-18',
                'authType': 'test_type',
                'appId': 'test_app_id',
                'publisherToken': 'test_publisher_token'
            })

        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['status'] == 'valid'
        assert json_data['publisherPlayerId'] == '12345'


def test_authenticate_player_invalid_facebook(client):
    with patch.object(signature_service, 'check_signature', return_value=True):
        mock_login = Mock()
        mock_login.is_valid = False

        with patch('controllers.auth.methods.facebook.requests.get', return_value=mock_login):
            response = client.post('/auth', json={
                'authMethod': 'facebook',
                'token': 'test_token',
                'date': '2021-08-18',
                'authType': 'test_type',
                'appId': 'test_app_id',
                'publisherToken': 'test_publisher_token'
            })

        assert response.status_code == 400
        assert response.data == b'Bad login'


def test_authenticate_player_invalid_auth_method(client):
    with patch.object(signature_service, 'check_signature', return_value=True):
        response = client.post('/auth', json={
            'authMethod': 'twitter',
            'token': 'test_token',
            'date': '2021-08-18',
            'authType': 'test_type',
            'appId': 'test_app_id',
            'publisherToken': 'test_publisher_token'
        })

    assert response.status_code == 400
    assert "Invalid login type: twitter" in str(response.data)
