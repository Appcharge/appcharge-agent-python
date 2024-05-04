import requests

from config.settings import get_settings


class PlayerService:
    player_url = get_settings().AWARD_PUBLISHER_URL
    publisher_token = get_settings().PUBLISHER_TOKEN

    def update_balance(self, request_body: bytes) -> dict:
        response = requests.post(
            url=self.player_url,
            headers={
                "Content-Type": "application/json",
                "x-publisher-token": self.publisher_token,
            },
            data=request_body,
        )
        return response.json()
