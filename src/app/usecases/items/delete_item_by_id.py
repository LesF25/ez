from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.domain import UseCase, RepositoryMixin
from src.app.schemas.items import DeleteItemByIdRequest, DeleteItemResponse


class DeleteItemByIdUseCase(
    RepositoryMixin[ItemRepository],
    UseCase[DeleteItemByIdRequest, DeleteItemResponse],
):
    async def _execute(self, dto: DeleteItemByIdRequest) -> DeleteItemResponse:
        status = await self._repository.delete_by_id(dto.item_id)
        return DeleteItemResponse(status=status)
