import dataclasses
from abc import abstractmethod
from datetime import datetime
from typing import Optional, Any

from src.app.domain.entities import ItemEntity
from .base_repository import AbstractRepository


@dataclasses.dataclass(frozen=True, slots=True)
class ItemCursorPayload:
    id: int
    created_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'ItemCursorPayload':
        return cls(
            id=data['id'],
            created_at=data['created_at'],
        )

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


class ItemRepositoryBase(
    AbstractRepository[ItemEntity, int],
):
    @abstractmethod
    async def find_all(
        self,
        limit: int,
        cursor_payload: Optional[ItemCursorPayload] = None
    ) -> list[ItemEntity]:
        ...
