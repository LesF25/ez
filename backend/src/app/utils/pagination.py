import base64
import json
from binascii import Error
from typing import Any

from .json_encoder import AdvancedJSONEncoder


class InvalidCursorError(Exception):
    ...


def encode_cursor(data: dict[str, Any]) -> str:
    payload = json.dumps(data, cls=AdvancedJSONEncoder)
    return base64.urlsafe_b64encode(payload.encode()).decode()


def decode_cursor(cursor: str) -> dict[str, Any]:
    payload = base64.urlsafe_b64decode(cursor.encode()).decode()
    return json.loads(payload)
