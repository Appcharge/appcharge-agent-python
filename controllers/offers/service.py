import requests

from config.settings import get_settings


class OffersService:
    offers_url = get_settings().ASSET_UPLOAD_GATEWAY_URL + "/offering/offer"
    popups_url = offers_url + "/popup/daily-bonus"
    publisher_token = get_settings().PUBLISHER_TOKEN

    def create_offer(self, request_body: bytes) -> dict:
        response = requests.post(
            url=self.offers_url,
            headers={
                "Content-Type": "application/json",
                "x-publisher-token": self.publisher_token,
            },
            data=request_body,
        )
        return response.json()

    def update_offer(self, offer_id: str, request_body: bytes) -> dict:
        response = requests.put(
            url=self.offers_url + "/" + offer_id,
            headers={
                "Content-Type": "application/json",
                "x-publisher-token": self.publisher_token,
            },
            data=request_body,
        )
        return response.json()

    def create_popup(self, request_body: bytes) -> dict:
        response = requests.post(
            url=self.popups_url,
            headers={
                "Content-Type": "application/json",
                "x-publisher-token": self.publisher_token,
            },
            data=request_body,
        )
        return response.json()

    def update_popup(self, popup_id: str, request_body: bytes) -> dict:
        response = requests.put(
            url=self.popups_url + "/" + popup_id,
            headers={
                "Content-Type": "application/json",
                "x-publisher-token": self.publisher_token,
            },
            data=request_body,
        )
        return response.json()
