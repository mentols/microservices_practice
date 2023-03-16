from fastapi import HTTPException
from starlette import status

from app.generics.uow import UnitOfWork
from app.models.pages import Page
from app.schemas.pages import PageIn as PageSchemaIn


# service
from producer import send_one


class PagesController:
    def __init__(self):
        self.uow = UnitOfWork()

    async def get_all_pages(self):
        async with self.uow:
            return await self.uow.pages.all()

    async def get_page(self, page_id):
        async with self.uow:
            page = await self.uow.pages.get(id=page_id)
            if page:
                return page
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Page is not exists",
            )

    async def create_page(self, page: PageSchemaIn, authorization):
        # owner_id = await TokenServices.decode_access_jwt_token(authorization)
        async with self.uow:
            owner_id = 1
            page = Page(owner_id=owner_id, **(page.dict()))
            await self.uow.pages.create(page)

    async def update_page(self, page_id: int, page: PageSchemaIn):
        async with self.uow:
            page_model = await self.uow.pages.get(id=page_id)
            page_model.name = page.name
            await self.uow.pages.update(page_model)

    async def delete_page(self, page_id):
        async with self.uow:
            self.uow.pages.delete(id=page_id)
            await send_one({'del': page_id})
