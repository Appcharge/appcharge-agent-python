import requests

from config.settings import get_settings


class OffersService:
    offers_url = get_settings().ASSET_UPLOAD_GATEWAY_URL + "/offering/offer"
    publisher_token = get_settings().PUBLISHER_TOKEN

    def create_offer(self, request_body: bytes, signature: str) -> dict:
        response = requests.post(
            url=self.offers_url,
            headers={
                "Content-Type": "application/json",
                "signature": signature,
                "x-publisher-token": self.publisher_token
            },
            data=request_body
        )
        return response.json()

    def update_offer(self, offer_id: str, request_body: bytes, signature: str) -> dict:
        response = requests.put(
            url=self.offers_url + "/" + offer_id,
            headers={
                "Content-Type": "application/json",
                "signature": signature,
                "x-publisher-token": self.publisher_token
            },
            data=request_body
        )
        return response.json()
