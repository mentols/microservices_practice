from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_session
from app.controller.tasks import TasksController
from app.schemas.tasks import TaskIn as TaskSchemaIn
from app.schemas.tasks import Task as TaskSchema


api_router = APIRouter()


@api_router.get('', response_model=List[TaskSchema])
async def get_all_tasks(page_id: int, session: AsyncSession = Depends(get_session)):
    tasks = await TasksController.get_all_tasks(page_id, session)
    return tasks


@api_router.post('')
async def create_task(page_id: int, task: TaskSchemaIn, session: AsyncSession = Depends(get_session)):
    await TasksController.create_task(page_id, task, session)


@api_router.get('/{task_id}', response_model=TaskSchema)
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task = await TasksController.get_task(task_id, session)
    return task


@api_router.patch('/{task_id}')
async def complete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    await TasksController.complete_task(task_id, session)


@api_router.delete('/{task_id}')
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    await TasksController.delete_task(task_id, session)
