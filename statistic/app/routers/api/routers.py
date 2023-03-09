from fastapi import APIRouter

from app.routers.api.v1.pages import api_router as pages_router

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(pages_router, prefix="/pages", tags=["pages"])
