from typing import List

from fastapi import HTTPException
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from app.models.pages import Page
from app.schemas.pages import Page as PageSchema
from app.services.tokens import TokenServices


class PagesRepository:
    @staticmethod
    async def create_page(page: dict, session: AsyncSession, authorization: str) -> None:
        owner_id = await TokenServices.decode_access_jwt_token(authorization)
        page = Page(name=page.get('name'), owner_id=owner_id)
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
    async def get_page(page_id, session: AsyncSession) -> PageSchema:
        result = await session.execute(select(Page).where(Page.id == page_id))
        page = result.scalars().first()
        if page:
            return page
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page is not exists",
        )

    @staticmethod
    async def get_all_pages(session: AsyncSession) -> List[PageSchema]:
        result = await session.execute(select(Page))
        return result.scalars().all()

    @staticmethod
    async def delete_page(page_id, session: AsyncSession) -> None:
        query = delete(Page).where(Page.id == page_id)
        await session.execute(query)
        await session.commit()
