from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, StringConstraints, Field, ConfigDict, field_serializer

ItemText = Annotated[
    str,
    StringConstraints(
        min_length=1,
        max_length=1000,
        strip_whitespace=True
    )
]


class CreateItemRequest(BaseModel):
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


class DeleteItemByIdRequest(BaseModel):
    item_id: int


class DeleteItemResponse(BaseModel):
    status: bool = True
