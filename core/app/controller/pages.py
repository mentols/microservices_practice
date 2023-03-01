from app.repository.pages import PagesRepository
from app.schemas.pages import PageIn as PageSchemaIn
from sqlalchemy.ext.asyncio import AsyncSession


class PagesController:
    @staticmethod
    async def get_all_pages(session: AsyncSession):
        pages = await PagesRepository.get_all_pages(session)
        return pages

    @staticmethod
    async def get_page(page_id, session: AsyncSession):
        page = await PagesRepository.get_page(page_id, session)
        return page

    @staticmethod
    async def create_page(page: PageSchemaIn, session: AsyncSession):
        await PagesRepository.create_page(page.dict(), session)

    @staticmethod
    async def update_page(page_id: int, page: PageSchemaIn, session: AsyncSession):
        await PagesRepository.update_page(page_id, page.dict(), session)

    @staticmethod
    async def delete_page(page_id, session: AsyncSession):
        await PagesRepository.delete_page(page_id, session)
