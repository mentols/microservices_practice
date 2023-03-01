from typing import List

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.pages import Page
from app.schemas.pages import Page as PageSchema


class PagesRepository:
    @staticmethod
    async def create_page(page: dict, session: AsyncSession) -> None:
        print(page)
        page = Page(name=page.get('name'))
        session.add(page)
        await session.commit()
        await session.refresh(page)

    @staticmethod
    async def update_page(page_id, page, session: AsyncSession) -> None:
        query = (
            update(Page).where(Page.id == page_id).values(**page).execution_options(synchronize_session="fetch")
        )

        await session.execute(query)
        await session.commit()

    @staticmethod
    async def get_page(page_id, session: AsyncSession):
        result = await session.execute(select(Page).where(Page.id == page_id))
        return result.scalars().first()

    @staticmethod
    async def get_all_pages(session: AsyncSession):
        result = await session.execute(select(Page))
        return result.scalars().all()
        # return [PageSchema(id=page.id, name=page.name) for page in pages]

    @staticmethod
    async def delete_page(page_id, session: AsyncSession) -> None:
        query = delete(Page).where(Page.id == page_id)
        await session.execute(query)
        await session.commit()
