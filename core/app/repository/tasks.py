from typing import List

from fastapi import HTTPException
from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from app.models.pages import Page
from app.models.tasks import Task, CompleteStatus
from app.schemas.tasks import Task as TaskSchema


class TasksRepository:
    @staticmethod
    async def get_all_tasks(page_id: int, session: AsyncSession) -> List[TaskSchema]:
        result = await session.execute(select(Task).where(Task.page_id == page_id))
        return result.scalars().all()

    @staticmethod
    async def create_task(page_id: int, task: dict, session: AsyncSession) -> None:
        query = await session.execute(select(Page).where(Page.id == page_id))
        page = query.scalars().first()
        task = Task(name=task.get('name'), page_id=page_id, page=page)
        session.add(task)
        await session.commit()
        await session.refresh(task)

    @staticmethod
    async def get_task(task_id: int, session: AsyncSession) -> TaskSchema:
        query = await session.execute(select(Task).where(Task.id == task_id))
        task = query.scalars().first()
        if task:
            return task
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task is not exists",
        )

    @staticmethod
    async def complete_task(task_id, session: AsyncSession) -> None:
        changed_status: list = []
        query = await session.execute(select(Task).where(Task.id == task_id))
        task = query.scalars().first()
        if not task:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task is not exists",
            )

        task_status = task.status
        [changed_status.append(st) if st != task_status else ... for st in CompleteStatus]
        query = (
            update(Task).where(Task.id == task_id)
                .values(status=changed_status[0])
                .execution_options(synchronize_session="fetch")
        )

        await session.execute(query)
        await session.commit()

    @staticmethod
    async def delete_task(task_id: int, session: AsyncSession) -> None:
        query = delete(Task).where(Task.id == task_id)
        await session.execute(query)
        await session.commit()
