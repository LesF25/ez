from abc import ABC, abstractmethod
from typing import TypeVar, Generic

EntityType = TypeVar('EntityType')
PrimaryKeyType = TypeVar('PrimaryKeyType')


class AbstractRepository(
    Generic[EntityType, PrimaryKeyType],
    ABC,
):
    @abstractmethod
    async def save(self, entity: EntityType) -> EntityType:
        ...

    @abstractmethod
    async def find_by_id(self, pk: PrimaryKeyType) -> EntityType | None:
        ...

    @abstractmethod
    async def delete_by_id(self, pk: PrimaryKeyType) -> bool:
        ...
