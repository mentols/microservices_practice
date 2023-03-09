from fastapi import APIRouter

from app.controller.pages import PagesController
from app.schemas.pages import Page as PageSchema

api_router = APIRouter()


@api_router.get('/{page_id}/statistic', response_model=PageSchema)
async def statistic(page_id: int):
    return await PagesController.statistic(page_id)


