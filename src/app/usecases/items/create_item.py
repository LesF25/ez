from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.core.domain import UseCase, RepositoryMixin
from src.app.entities.item import ItemEntity
from src.app.schemas.items import CreateItemRequest, ItemResponse


class CreateItemUseCase(
    RepositoryMixin[ItemRepository],
    UseCase[CreateItemRequest, ItemResponse],
):
    async def _execute(self, dto: CreateItemRequest) -> ItemResponse:
        entity = ItemEntity(text=dto.text)
        entity = await self._repository.save(entity)

        return ItemResponse.model_validate(entity)
