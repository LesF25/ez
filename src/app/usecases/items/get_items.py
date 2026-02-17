from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.domain import UseCase, RepositoryMixin
from src.app.schemas.items import ItemResponse
from src.app.schemas.common import PaginationRequest


class GetItemsUseCase(
    RepositoryMixin[ItemRepository],
    UseCase[PaginationRequest, list[ItemResponse]],
):
    async def _execute(self, dto: PaginationRequest) -> list[ItemResponse]:
        items_gen = self._repository.find_all(
            limit=dto.limit,
            offset=(dto.page - 1) * dto.limit,
        )

        return [
            ItemResponse.model_validate(item)
            async for item in items_gen
        ]
