from typing import List

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.pages import Page
from app.schemas.pages import Page as PageSchema
from app.schemas.pages import PageIn as PageSchemaIn

from producer import send_one


# todo: contextvar
# todo: decode_access_jwt_token in controller


class PagesRepository:
    @staticmethod
    async def create(page: PageSchema, session: AsyncSession) -> None:
        session.add(page)
        await session.commit()
        await session.refresh(page.dict())
        await send_one({'add': page.id})

    @staticmethod
    async def update(page_id: int, page: PageSchemaIn, session: AsyncSession) -> None:
        query = (
            update(Page).where(Page.id == page_id).values(**page).execution_options(synchronize_session="fetch")
        )
        await session.execute(query)
        await session.commit()

    @staticmethod
    async def get(page_id, session: AsyncSession) -> PageSchema:
        result = await session.execute(select(Page).where(Page.id == page_id))
        page = result.scalars().first()
        return page

    @staticmethod
    async def all(session: AsyncSession) -> List[PageSchema]:
        result = await session.execute(select(Page))
        return result.scalars().all()

    @staticmethod
    async def delete(page_id, session: AsyncSession) -> None:
        query = delete(Page).where(Page.id == page_id)
        await session.execute(query)
        await session.commit()
        await send_one({'del': page_id})
