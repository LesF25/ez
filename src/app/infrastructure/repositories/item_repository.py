from typing import AsyncGenerator

from sqlalchemy import Result, insert, select, delete

from src.core.domain.repository import PrimaryKeyType, EntityType
from src.core.infrastructure.postgres.models import Item
from src.app.entities.item import ItemEntity
from src.app.infrastructure.repositories.repository import (
    SQLAlchemyAbstractRepository
)


class ItemMapper:
    def to_domain(self, model: Item) -> ItemEntity:
        return ItemEntity(
            id=model.id,
            text=model.text,
            created_at=model.created_at,
        )


class ItemRepository(SQLAlchemyAbstractRepository):
    MAPPER = ItemMapper()

    async def save(self, entity: ItemEntity) -> ItemEntity:
        result: Result = await self._session.execute(
            insert(Item)
            .values(text=entity.text)
            .returning(Item)
        )
        item = result.scalar_one()

        return self.MAPPER.to_domain(item)

    async def find_all(self, limit: int, offset: int) -> AsyncGenerator[ItemEntity, None]:
        result = await self._session.stream_scalars(
            select(Item)
            .limit(limit)
            .offset(offset)
        )

        async for item in result:
            yield self.MAPPER.to_domain(item)

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
