import datetime
import json
from typing import Any


class AdvancedJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        return super().default(obj)
