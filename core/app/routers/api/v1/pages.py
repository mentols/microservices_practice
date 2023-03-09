from typing import List

from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import Response

from app.controller.pages import PagesController
from app.database.db import get_session
from app.schemas.pages import Page as PageSchema
from app.schemas.pages import PageIn as PageSchemaIn

api_router = APIRouter()


@api_router.get('', response_model=List[PageSchema])
async def get_all_pages(session: AsyncSession = Depends(get_session)):
    pages = await PagesController.get_all_pages(session)
    return pages


@api_router.post('')
async def create_page(page: PageSchemaIn, session: AsyncSession = Depends(get_session),
                      authorization: str = Header(None)):
    await PagesController.create_page(page, session, authorization)
    return Response(status_code=status.HTTP_200_OK)


@api_router.get('/{page_id}', response_model=PageSchema)
async def get_page(page_id: int, session: AsyncSession = Depends(get_session)):
    page = await PagesController.get_page(page_id, session)
    return page


@api_router.put('/{page_id}')
async def update_page(page_id: int, page: PageSchemaIn, session: AsyncSession = Depends(get_session)):
    await PagesController.update_page(page_id, page, session)
    return Response(status_code=status.HTTP_200_OK)


@api_router.delete('/{page_id}')
async def delete_page(page_id: int, session: AsyncSession = Depends(get_session)):
    await PagesController.delete_page(page_id, session)
    return Response(status_code=status.HTTP_200_OK)
