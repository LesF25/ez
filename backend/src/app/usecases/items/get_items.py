from alembic.operations.toimpl import drop_table

from src.app.domain.entities import ItemEntity
from src.app.domain.repositories import ItemCursorPayload, ItemRepositoryBase
from src.app.domain.use_case import UseCase, UseCaseRepositoryMixin
from src.app.schemas.items import ItemResponse, ItemPaginationResponse, ItemPaginationRequest
from src.app.utils.pagination import encode_cursor


class GetItemsUseCase(
    UseCaseRepositoryMixin[ItemRepositoryBase],
    UseCase[ItemPaginationRequest, ItemPaginationResponse],
):
    async def _execute(self, dto: ItemPaginationRequest) -> ItemPaginationResponse:
        cursor_payload = (
            ItemCursorPayload(
                id=dto.cursor.id,
                created_at=dto.cursor.created_at,
            )
            if dto.cursor else None
        )

        items = await self._repository.find_all(
            limit=dto.limit + 1,
            cursor_payload=cursor_payload,
        )

        has_next = len(items) > dto.limit
        items = items[:dto.limit]

        next_cursor = (
            self._get_next_cursor(items[-1])
            if has_next else None
        )

        return ItemPaginationResponse(
            items=[ItemResponse.model_validate(item) for item in items],
            next_cursor=next_cursor,
        )

    def _get_next_cursor(self, item: ItemEntity) -> str:
        cursor_payload = ItemCursorPayload(
            created_at=item.created_at,
            id=item.id,
        )
        return encode_cursor(cursor_payload.to_dict())
