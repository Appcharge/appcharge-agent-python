from app import app
import json
from flask import request, jsonify
from .methods.facebook import facebook_login
from .models import *
from app import APP_SECRET
import os



@app.route('/auth', methods=['POST'])
def authenticate_player():
    auth_request = AuthenticationRequest.from_json(request.data)
    auth_method = auth_request.auth_method

    login_result = LoginResponse(False, 0)
    
    if auth_method == 'facebook':
        login_result = facebook_login(APP_SECRET, auth_request.app_id, auth_request.token)
    else:
        raise Exception(f'Invalid login type: {auth_method}')

    if login_result.is_valid:
        print(f"Player with id {login_result.user_id} logged in successfully")
        response = AuthenticationResponse("valid", "", login_result.user_id, "player name", ["segment1", "segment2"], [
            {
                "currency": "diamonds",
                "balance": 456
            },
            {
                "currency": "stones",
                "balance": 6
            }
        ])

        return response.to_json()
    else:
        print(f"Player with token {auth_request.token} failed to log in")
        return "Bad login", 400