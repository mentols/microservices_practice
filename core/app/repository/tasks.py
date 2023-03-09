from typing import List

from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.tasks import Task
from app.schemas.tasks import Task as TaskSchema
from producer import send_one


class TasksRepository:
    @staticmethod
    async def all(page_id: int, session: AsyncSession) -> List[TaskSchema]:
        result = await session.execute(select(Task).where(Task.page_id == page_id))
        return result.scalars().all()

    @staticmethod
    async def create(page_id: int, task: Task, session: AsyncSession) -> None:
        session.add(task)
        await session.commit()
        await session.refresh(task)
        await send_one({'add_t': page_id})

    @staticmethod
    async def get(task_id: int, session: AsyncSession) -> TaskSchema:
        query = await session.execute(select(Task).where(Task.id == task_id))
        return query.scalars().first()

    @staticmethod
    async def complete(task: TaskSchema, session: AsyncSession) -> None:
        query = (
            update(Task).where(Task.id == task.id)
                .values(**task)
                .execution_options(synchronize_session="fetch")
        )

        await session.execute(query)
        await session.commit()
        await send_one({'upd': task.page_id})

    @staticmethod
    async def delete(task_id: int, session: AsyncSession) -> None:
        query = delete(Task).where(Task.id == task_id)
        await session.execute(query)
        await session.commit()
