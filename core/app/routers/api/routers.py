from fastapi import APIRouter

from app.routers.api.v1.pages import PageRouter
from app.routers.api.v1.tasks import TaskRouter

tasks_router = TaskRouter()
pages_router = PageRouter()

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(pages_router.api_router, prefix="/pages", tags=["pages"])
v1_router.include_router(tasks_router.api_router, prefix="/pages/{page_id}/tasks", tags=["tasks"])
