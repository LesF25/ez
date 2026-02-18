from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.domain.use_case import UseCase, UseCaseRepositoryMixin
from src.app.schemas.items import ItemDeleteByIdRequest, ItemDeleteResponse


class DeleteItemByIdUseCase(
    UseCaseRepositoryMixin[ItemRepository],
    UseCase[ItemDeleteByIdRequest, ItemDeleteResponse],
):
    async def _execute(self, dto: ItemDeleteByIdRequest) -> ItemDeleteResponse:
        status = await self._repository.delete_by_id(dto.item_id)
        return ItemDeleteResponse(status=status)
