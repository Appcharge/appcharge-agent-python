import requests

from config.settings import get_settings


class PlayerService:
    player_url = get_settings().AWARD_PUBLISHER_URL
    publisher_token = get_settings().PUBLISHER_TOKEN

    def update_balance(self, request_body: bytes, signature: str) -> dict:
        response = requests.post(
            url=self.player_url,
            headers={
                "Content-Type": "application/json",
                "signature": signature,
            },
            data=request_body
        )
        return response.json()
