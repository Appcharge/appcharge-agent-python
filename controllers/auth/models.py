class AuthenticationRequest:
    def __init__(self, auth_method: str, token: str, date: str, auth_type: str, app_id: str, publisher_token: str):
        self.auth_method = auth_method
        self.token = token
        self.date = date
        self.auth_type = auth_type
        self.app_id = app_id
        self.publisher_token = publisher_token

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(
            auth_method=json_data.get('authMethod'),
            token=json_data.get('token'),
            date=json_data.get('date'),
            auth_type=json_data.get('authType'),
            app_id=json_data.get('appId'),
            publisher_token=json_data.get('publisherToken'),
        )

    def to_json(self) -> dict:
        return {
            'authMethod': self.auth_method,
            'token': self.token,
            'date': self.date,
            'authType': self.auth_type,
            'appId': self.app_id,
            'publisherToken': self.publisher_token,
        }


class LoginResponse:
    def __init__(self, is_valid, user_id):
        self.is_valid = is_valid
        self.user_id = user_id


class AuthenticationResponse:
    def __init__(self, status, player_profile_image, publisher_player_id, player_name, segments, balances):
        self.status = status
        self.player_profile_image = player_profile_image
        self.publisher_player_id = publisher_player_id
        self.player_name = player_name
        self.segments = segments
        self.balances = balances

    def to_json(self):
        return {
            'status': self.status,
            'playerProfileImage': self.player_profile_image,
            'publisherPlayerId': self.publisher_player_id,
            'playerName': self.player_name,
            'segments': self.segments,
            'balances': self.balances
        }

