from datetime import datetime
import hmac
import hashlib
import json
import re

from config.settings import get_settings

class SignatureService:
    key = get_settings().KEY.encode("utf-8")

    def _get_signature(self, payload: bytes) -> str:
        signature = hmac.new(self.key, msg=payload, digestmod=hashlib.sha256).hexdigest()
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
    
    def create_signature(self, payload: bytes):
        timestamp = str(int(datetime.utcnow().timestamp()))
        serialized_payload = self._serialize_payload(payload, timestamp)
        expected_signature = self._get_signature(serialized_payload)
        return f"t={timestamp},v1={expected_signature}"
