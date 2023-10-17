import requests

from config.settings import get_settings


class AnalyticsService:
    analytics_url = get_settings().REPORTING_API_URL + "/reporting/reports/analytics"
    publisher_token = get_settings().PUBLISHER_TOKEN

    def get_analytics(self, request_body: bytes, signature: str) -> dict:
        response = requests.post(
            url=self.analytics_url,
            headers={
                "Content-Type": "application/json",
                "signature": signature,
                "x-publisher-token": self.publisher_token
            },
            data=request_body
        )
        return response.json()
