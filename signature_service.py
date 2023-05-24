import hmac
import hashlib
import json


class SignatureService:
    def __init__(self, key):
        self.key = key.encode("utf8")

    def _get_signature(self, payload: bytes) -> str:
        digest = hmac.new(self.key, msg=payload, digestmod=hashlib.sha256).digest()
        signature = digest.hex()
        return signature

    @staticmethod
    def _serialize_payload(payload: bytes) -> bytes:
        serialized_payload = json.loads(payload)
        serialized_payload = str(serialized_payload)
        serialized_payload = serialized_payload.replace("\'", "\"").replace(" ", "")
        return serialized_payload.encode("utf8")

    def check_signature(self, payload: bytes, signature: str) -> bool:
        serialized_payload = self._serialize_payload(payload)
        expected_signature = self._get_signature(serialized_payload)
        return expected_signature == signature
