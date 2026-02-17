from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.core.infrastructure.postgres import get_session, get_transaction_session


def get_item_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> ItemRepository:
    return ItemRepository(session)


def get_item_repository_tx(
    session: Annotated[AsyncSession, Depends(get_transaction_session)]
) -> ItemRepository:
    return ItemRepository(session)
