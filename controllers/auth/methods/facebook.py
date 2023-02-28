import requests
from ..models import LoginResponse

def facebook_login(app_secret, app_id, token):
    url = f'https://graph.facebook.com/debug_token?input_token={token}&access_token={app_id}|{app_secret}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        is_valid = data['data']['is_valid']
        user_id = data['data']['user_id']
        return LoginResponse(is_valid, user_id)
    else:
        return LoginResponse(False, "0")
