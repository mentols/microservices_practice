from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.models.pages import Page
from app.repository.pages import PagesRepository
from app.schemas.pages import PageIn as PageSchemaIn


class PagesController:
    @staticmethod
    async def get_all_pages(session: AsyncSession):
        pages = await PagesRepository.all(session)
        return pages

    @staticmethod
    async def get_page(page_id, session: AsyncSession):
        page = await PagesRepository.get(page_id, session)
        if page:
            return page
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page is not exists",
        )

    @staticmethod
    async def create_page(page: PageSchemaIn, session: AsyncSession, authorization):
        # owner_id = await TokenServices.decode_access_jwt_token(authorization)
        owner_id = 1
        page = Page(owner_id=owner_id, **(page.dict()))
        await PagesRepository.create(page.dict(), session)

    @staticmethod
    async def update_page(page_id: int, page: PageSchemaIn, session: AsyncSession):
        await PagesRepository.update(page_id, page, session)

    @staticmethod
    async def delete_page(page_id, session: AsyncSession):
        await PagesRepository.delete(page_id, session)
