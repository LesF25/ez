from typing import Annotated
from fastapi import APIRouter, status
from fastapi.params import Depends, Body, Query, Path

from src.app.infrastructure.repositories.item_repository import ItemRepository
from src.app.schemas.items import (
    ItemCreateRequest,
    ItemResponse,
    ItemDeleteResponse,
    ItemDeleteByIdRequest,
    ItemPaginationResponse, ItemPaginationRequest,
)
from src.app.usecases.items import (
    CreateItemUseCase,
    DeleteItemByIdUseCase,
    GetItemsUseCase,
)
from .dependency import get_item_repository, get_item_repository_tx, validate_cursor

router = APIRouter(prefix='/items')


@router.post(
    path='',
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(
    dto: Annotated[ItemCreateRequest, Body()],
    repository: Annotated[ItemRepository, Depends(get_item_repository_tx)],
) -> ItemResponse:
    use_case = CreateItemUseCase(repository)

    return await use_case.execute(dto)


@router.get(
    path='',
    response_model=ItemPaginationResponse,
    status_code=status.HTTP_200_OK,
)
async def get_items(
    dto: Annotated[ItemPaginationRequest, Depends(validate_cursor)],
    repository: Annotated[ItemRepository, Depends(get_item_repository)],
) -> ItemPaginationResponse:
    use_case = GetItemsUseCase(repository)

    return await use_case.execute(dto)


@router.delete(
    path='/{item_id}',
    response_model=ItemDeleteResponse,
    status_code=status.HTTP_200_OK,
)
async def delete_item_by_id(
    dto: Annotated[ItemDeleteByIdRequest, Path()],
    repository: Annotated[ItemRepository, Depends(get_item_repository_tx)],
) -> ItemDeleteResponse:
    use_case = DeleteItemByIdUseCase(repository)

    return await use_case.execute(dto)
