from typing import List

from fastapi import HTTPException
from starlette import status

from app.generics.uow import UnitOfWork
from app.models.pages import Page
from app.permissions.tokens import TokenServices
from app.schemas.pages import PageIn as PageSchemaIn
from producer import send_one


class PagesServices:
    def __init__(self):
        self.uow = UnitOfWork()

    async def get_all_pages(self) -> List[Page]:
        async with self.uow:
            return await self.uow.pages.all()

    async def get_page(self, page_id) -> Page:
        async with self.uow:
            page = await self.uow.pages.get(id=page_id)
            if page:
                return page
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Page is not exists",
            )

    async def create_page(self, page: PageSchemaIn, authorization) -> None:
        # todo: get user id with auth_microservice endpoint
        owner_id = await TokenServices.decode_access_jwt_token(authorization)
        async with self.uow:
            page = Page(owner_id=owner_id, **(page.dict()))
            page_id = await self.uow.pages.create(page)
            await send_one({'add': page_id})

    async def update_page(self, page_id: int, page: PageSchemaIn) -> None:
        async with self.uow:
            page_model = await self.uow.pages.get(id=page_id)
            page_model.name = page.name
            await self.uow.pages.update(page_model)

    async def delete_page(self, page_id) -> None:
        async with self.uow:
            await self.uow.pages.delete(id=page_id)
            await send_one({'del': page_id})
