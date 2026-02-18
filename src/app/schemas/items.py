from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints, ConfigDict, field_serializer

ItemText = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=1000,
        strip_whitespace=True
    )
]


class ItemCreateRequest(BaseModel):
    text: ItemText


class ItemResponse(BaseModel):
    id: int
    text: ItemText
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )

    @field_serializer('created_at')
    def serialize_dt(self, created_at: datetime) -> str:
        created_at = created_at.replace(microsecond=0, tzinfo=None)
        return created_at.isoformat()


class ItemDeleteByIdRequest(BaseModel):
    item_id: int


class ItemDeleteResponse(BaseModel):
    status: bool = True


class ItemCursor(BaseModel):
    id: int
    created_at: datetime


class ItemPaginationRequest(BaseModel):
    limit: int
    cursor: Optional[ItemCursor] = None


class ItemPaginationResponse(BaseModel):
    items: list[ItemResponse]
    next_cursor: str | None = None
