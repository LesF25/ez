import binascii
from typing import Annotated

from fastapi import HTTPException, status
from fastapi.params import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.infrastructure.postgres import get_session, get_transaction_session
from src.app.schemas.common import PaginationRequest
from src.app.schemas.items import ItemPaginationRequest, ItemCursor
from src.app.utils.pagination import decode_cursor


def get_item_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> ItemRepository:
    return ItemRepository(session)


def get_item_repository_tx(
    session: Annotated[AsyncSession, Depends(get_transaction_session)]
) -> ItemRepository:
    return ItemRepository(session)


def validate_cursor(
    params: Annotated[PaginationRequest, Query()],
) -> ItemPaginationRequest:
    if params.next_cursor is None:
        return ItemPaginationRequest(limit=params.limit, cursor=None)

    try:
        payload = decode_cursor(params.next_cursor)
        cursor = ItemCursor.model_validate(payload)
    except (
        binascii.Error,
        ValueError,
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid cursor"
        )

    return ItemPaginationRequest(limit=params.limit, cursor=cursor)
