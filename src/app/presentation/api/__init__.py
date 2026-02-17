from fastapi import APIRouter
from src.app.presentation.api.items.items import router as items_router

router = APIRouter(prefix='/api')
router.include_router(items_router)
