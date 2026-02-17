from typing import Annotated, Literal

from pydantic import BaseModel, Field


class PaginationRequest(BaseModel):
    page: int = Field(ge=1)
    limit: Annotated[
        int, Literal[10, 20, 30]
    ] = 20
