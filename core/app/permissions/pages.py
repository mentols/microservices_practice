import logging

from fastapi import HTTPException, status, Header, Depends
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.generics.uow import UnitOfWork
from app.repository.pages import PagesRepository
from app.repository.tasks import TasksRepository
from app.permissions.tokens import TokenServices

logger = logging.getLogger(__name__)


class Permissions:
    def __init__(self):
        self.uow = UnitOfWork()

    async def check_page_permission(self, request: Request, authorization: str = Header(None)):
        await self.check_page(request, authorization, -1)

    async def check_task_permission(self, request: Request, authorization: str = Header(None)):
        if request.url.path.split('/')[-1] == 'tasks':
            await self.check_page(request, authorization, -2)
        else:
            await self.check_page(request, authorization, -3)
            await self.check_task(request, -1)

    async def check_page(self, request, authorization, index):
        page_id = int(request.url.path.split('/')[index])
        user_id = await TokenServices.decode_access_jwt_token(authorization)
        async with self.uow:
            page = await self.uow.pages.get(id=page_id)
            if page.owner_id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Has no permission to perform this operation",
                )

    async def check_task(self, request, index):
        task_id = int(request.url.path.split('/')[index])
        async with self.uow:
            task = await self.uow.tasks.get(id=task_id)
            if task.page_id != int(request.url.path.split('/')[-3]):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Task does not belong to the page",
                )
