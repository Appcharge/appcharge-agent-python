import hmac
import hashlib
import json
import re


class SignatureService:
    def __init__(self, key):
        self.key = key.encode("utf8")

    def _get_signature(self, payload: bytes) -> str:
        digest = hmac.new(self.key, msg=payload, digestmod=hashlib.sha256).digest()
        signature = digest.hex()
        return signature

    @staticmethod
    def _serialize_payload(payload: bytes, timestamp: str) -> bytes:
        payload_dict = json.loads(payload)
        payload_string = json.dumps(payload_dict, separators=(',', ':'), ensure_ascii=False)
        serialized_payload = f"{timestamp}.{payload_string}"
        return serialized_payload.encode("utf8")

    @staticmethod
    def _parse_signature(signature: str) -> tuple[str, str]:
        regex = re.compile(r"t=(.*),v1=(.*)")
        match = regex.match(signature)
        if not match or len(match.groups()) < 2:
            raise ValueError("Invalid signature format")
        timestamp = match.group(1)
        signature = match.group(2)
        return timestamp, signature

    def check_signature(self, payload: bytes, signature: str) -> bool:
        timestamp, signature = self._parse_signature(signature)
        serialized_payload = self._serialize_payload(payload, timestamp)
        expected_signature = self._get_signature(serialized_payload)
        return expected_signature == signature
