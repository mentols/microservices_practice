from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.tasks import TasksRepository
from app.schemas.tasks import TaskIn as TaskSchemaIn


class TasksDomain:
    @staticmethod
    async def get_all_tasks(page_id: int, session: AsyncSession):
        tasks = await TasksRepository.get_all_tasks(page_id, session)
        return tasks

    @staticmethod
    async def create_task(page_id: int, task: TaskSchemaIn, session: AsyncSession):
        await TasksRepository.create_task(page_id, task.dict(), session)

    @staticmethod
    async def get_task(task_id: int, session: AsyncSession):
        task = await TasksRepository.get_task(task_id, session)
        return task

    @staticmethod
    async def complete_task(task_id: int, session: AsyncSession):
        await TasksRepository.complete_task(task_id, session)

    @staticmethod
    async def delete_task(task_id, session: AsyncSession):
        await TasksRepository.delete_task(task_id, session)
