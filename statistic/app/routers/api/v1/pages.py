from fastapi import APIRouter

from app.controller.pages import PagesController
from app.schemas.pages import Page as PageSchema


class PageRouter:
    def __init__(self, client):
        self.api_router = APIRouter()
        self._register_routes()
        self.controller = PagesController(client)

    def _register_routes(self):
        @self.api_router.get('/{page_id}/statistic', response_model=PageSchema)
        async def statistic(page_id: int):
            return await self.controller.statistic(page_id)
