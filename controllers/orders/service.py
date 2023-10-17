import requests

from config.settings import get_settings


class OrdersService:
    orders_url = get_settings().REPORTING_API_URL + "/reporting/reports/orders"
    publisher_token = get_settings().PUBLISHER_TOKEN

    def get_orders(self, request_body: bytes, signature: str) -> dict:
        response = requests.post(
            url=self.orders_url,
            headers={
                "Content-Type": "application/json",
                "signature": signature,
                "x-publisher-token": self.publisher_token
            },
            data=request_body
        )
        return response.json()
