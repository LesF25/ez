from typing import Optional

from pydantic import BaseModel, Field


class PaginationRequest(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)
    next_cursor: Optional[str] = None
