from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.domain.use_case import UseCase, UseCaseRepositoryMixin
from src.app.domain.entities import ItemEntity
from src.app.schemas.items import ItemCreateRequest, ItemResponse


class CreateItemUseCase(
    UseCaseRepositoryMixin[ItemRepository],
    UseCase[ItemCreateRequest, ItemResponse],
):
    async def _execute(self, dto: ItemCreateRequest) -> ItemResponse:
        entity = ItemEntity(text=dto.text)
        entity = await self._repository.save(entity)

        return ItemResponse.model_validate(entity)
