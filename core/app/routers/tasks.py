from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.domain.tasks import TasksDomain
from app.schemas.tasks import TaskIn as TaskSchemaIn
api_router = APIRouter(prefix='/api/v1/pages/{page_id}/tasks')


@api_router.get('')
async def get_all_tasks(page_id: int, session: AsyncSession = Depends(get_session)):
    tasks = await TasksDomain.get_all_tasks(page_id, session)
    return tasks


@api_router.post('')
async def create_task(page_id: int, task: TaskSchemaIn, session: AsyncSession = Depends(get_session)):
    await TasksDomain.create_task(page_id, task, session)


@api_router.get('/{task_id}')
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task = await TasksDomain.get_task(task_id, session)
    return task


@api_router.patch('/{task_id}')
async def complete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    await TasksDomain.complete_task(task_id, session)


@api_router.delete('/{task_id}')
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    await TasksDomain.delete_task(task_id, session)
