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
    def _serialize_payload(payload: bytes, timestamp: str) -> bytes:
        serialized_payload = json.loads(payload)
        serialized_payload = str(serialized_payload)
        serialized_payload = serialized_payload.replace("\'", "\"").replace(" ", "")
        serialized_payload = f"{timestamp}.{serialized_payload}"
        return serialized_payload.encode("utf8")

    @staticmethod
    def _serialize_signature(signature: str) -> tuple[str, str]:
        signature_parts = signature.split(",")
        timestamp = signature_parts[0].replace("t=", "")
        signature = signature_parts[1].replace("v1=", "")
        return timestamp, signature

    def check_signature(self, payload: bytes, signature: str) -> bool:
        timestamp, signature = self._serialize_signature(signature)
        serialized_payload = self._serialize_payload(payload, timestamp)
        expected_signature = self._get_signature(serialized_payload)
        return expected_signature == signature
