from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.domain.pages import PagesDomain
from app.schemas.pages import PageIn as PageSchemaIn
from app.schemas.pages import Page as PageSchema

api_router = APIRouter(prefix='/api/v1')


@api_router.get('/pages', response_model=List[PageSchema])
async def get_all_pages(session: AsyncSession = Depends(get_session)):
    pages = await PagesDomain.get_all_pages(session)
    return pages


@api_router.post('/pages')
async def create_page(page: PageSchemaIn, session: AsyncSession = Depends(get_session)):
    await PagesDomain.create_page(page, session)


@api_router.get('/pages/{page_id}', response_model=PageSchema)
async def get_page(page_id: int, session: AsyncSession = Depends(get_session)):
    page = await PagesDomain.get_page(page_id, session)
    return page


@api_router.put('/pages/{page_id}')
async def update_page(page_id: int, page: PageSchemaIn, session: AsyncSession = Depends(get_session)):
    await PagesDomain.update_page(page_id, page, session)


@api_router.delete('/pages/{page_id}')
async def delete_page(page_id: int, session: AsyncSession = Depends(get_session)):
    await PagesDomain.delete_page(page_id, session)
