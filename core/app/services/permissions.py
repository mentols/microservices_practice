import logging

from fastapi import HTTPException, status, Header, Depends
from fastapi import Request
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.db import get_session
from app.repository.pages import PagesRepository
from app.repository.tasks import TasksRepository
from app.services.tokens import TokenServices

logger = logging.getLogger(__name__)


class Permissions:
    @staticmethod
    async def check_page_permission(request: Request, authorization: str = Header(None),
                                    session: AsyncSession = Depends(get_session)):
        await Permissions.check_page(request, authorization, session, -1)

    @staticmethod
    async def check_task_permission(request: Request, authorization: str = Header(None), session: AsyncSession = Depends(get_session)):
        print(request.url.path.split('/'))

        if request.url.path.split('/')[-1] == 'tasks':
            await Permissions.check_page(request, authorization, session, -2)
        else:
            await Permissions.check_page(request, authorization, session, -3)
            await Permissions.check_task(request, session, -1)

    @staticmethod
    async def check_page(request, authorization, session, index):
        page_id = int(request.url.path.split('/')[index])
        user_id = await TokenServices.decode_access_jwt_token(authorization)
        page = await PagesRepository.get_page(page_id, session)
        if page.owner_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Has no permission to perform this operation",
            )

    @staticmethod
    async def check_task(request, session, index):
        task_id = int(request.url.path.split('/')[index])
        task = await TasksRepository.get_task(task_id, session)
        if task.page_id != int(request.url.path.split('/')[-3]):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Task does not belong to the page",
            )
