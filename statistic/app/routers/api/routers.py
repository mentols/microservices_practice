from fastapi import APIRouter

from app.database.mongo import get_db as db
from app.routers.api.v1.pages import PageRouter

pages_router = PageRouter(await db())

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(pages_router.api_router, prefix="/pages", tags=["pages"])
