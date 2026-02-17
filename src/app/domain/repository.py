from abc import ABC, abstractmethod
from typing import TypeVar

EntityType = TypeVar('EntityType')
PrimaryKeyType = TypeVar('PrimaryKeyType')


class AbstractRepository(ABC):
    @abstractmethod
    async def save(self, entity: EntityType) -> EntityType:
        ...

    @abstractmethod
    async def find_by_id(self, pk: PrimaryKeyType) -> EntityType | None:
        ...

    @abstractmethod
    async def find_all(self, limit: int, offset: int) -> list[EntityType]:
        ...

    @abstractmethod
    async def delete_by_id(self, pk: PrimaryKeyType) -> bool:
        ...
