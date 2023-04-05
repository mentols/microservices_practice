from fastapi import APIRouter

from app.routers.api.v1.users import api_router as users_router

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(users_router, prefix="/auth", tags=["auth"])
