from typing import List

from fastapi import APIRouter, Header
from starlette import status
from starlette.responses import Response

from app.schemas.pages import Page as PageSchema
from app.schemas.pages import PageIn as PageSchemaIn
from app.services.pages import PagesServices


class PageRouter:
    def __init__(self):
        self.api_router = APIRouter()
        self._register_routes()
        self.service = PagesServices()

    def _register_routes(self):
        @self.api_router.get('', response_model=List[PageSchema])
        async def get_all_pages():
            pages = await self.service.get_all_pages()
            return pages

        @self.api_router.post('')
        async def create_page(page: PageSchemaIn, authorization: str = Header(None)):
            await PagesServices().create_page(page, authorization)
            return Response(status_code=status.HTTP_200_OK)

        @self.api_router.get('/{page_id}', response_model=PageSchema)
        async def get_page(page_id: int):
            page = await self.service.get_page(page_id)
            return page

        @self.api_router.put('/{page_id}')
        async def update_page(page_id: int, page: PageSchemaIn):
            await self.service.update_page(page_id, page)
            return Response(status_code=status.HTTP_200_OK)

        @self.api_router.delete('/{page_id}')
        async def delete_page(page_id: int):
            await self.service.delete_page(page_id)
            return Response(status_code=status.HTTP_200_OK)
