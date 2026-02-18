from datetime import datetime
from typing import AsyncGenerator, Optional

from sqlalchemy import Result, insert, select, delete, tuple_

from src.app.domain.repositories.item_repository import ItemRepositoryBase, ItemCursorPayload
from src.app.infrastructure.postgres.models import Item
from src.app.domain.entities import ItemEntity
from src.app.infrastructure.repositories import (
    SQLAlchemyAbstractRepository
)


class ItemMapper:
    def to_domain(self, model: Item) -> ItemEntity:
        return ItemEntity(
            id=model.id,
            text=model.text,
            created_at=model.created_at,
        )


class ItemRepository(
    SQLAlchemyAbstractRepository,
    ItemRepositoryBase,
):
    MAPPER = ItemMapper()

    async def save(self, entity: ItemEntity) -> ItemEntity:
        result: Result = await self._session.execute(
            insert(Item)
            .values(text=entity.text)
            .returning(Item)
        )
        item = result.scalar_one()

        return self.MAPPER.to_domain(item)

    async def find_all(
        self,
        limit: int,
        cursor_payload: Optional[ItemCursorPayload] = None,
    ) -> list[ItemEntity]:
        stmt = (
            select(Item)
            .order_by(Item.created_at.desc(), Item.id.desc())
            .limit(limit)
        )

        if cursor_payload:
            stmt = stmt.where(
                tuple_(Item.created_at, Item.id)
                < tuple_(cursor_payload.created_at, cursor_payload.id)
            )

        result = await self._session.stream_scalars(stmt)

        return [
            self.MAPPER.to_domain(item)
            async for item in result
        ]

    async def delete_by_id(self, pk: int) -> bool:
        result: Result = await self._session.execute(
            delete(Item)
            .filter_by(id=pk)
            .returning(Item.id)
        )
        item_id = result.scalar_one_or_none()

        return item_id is not None

    async def find_by_id(self, pk: int) -> ItemEntity | None:
        item: Item | None = await self._session.get(Item, pk)

        return self.MAPPER.to_domain(item) if item else None
