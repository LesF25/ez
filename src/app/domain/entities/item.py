from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True, slots=True)
class ItemEntity:
    text: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None
