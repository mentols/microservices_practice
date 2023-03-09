from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.enum.tasks import CompleteStatus
from app.models.tasks import Task
from app.repository.tasks import TasksRepository
from app.schemas.tasks import Task as TaskSchema
from app.schemas.tasks import TaskIn as TaskSchemaIn


class TasksController:
    @staticmethod
    async def get_all_tasks(page_id: int, session: AsyncSession):
        tasks = await TasksRepository.all(page_id, session)
        return tasks

    @staticmethod
    async def create_task(page_id: int, task: TaskSchemaIn, session: AsyncSession):
        task = Task(page_id=page_id, **(task.dict()))
        await TasksRepository.create(page_id, task.dict(), session)

    @staticmethod
    async def get_task(task_id: int, session: AsyncSession):
        task = await TasksRepository.get(task_id, session)
        if task:
            return task
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task is not exists",
        )

    @staticmethod
    async def complete_task(task_id: int, session: AsyncSession):
        changed_status: list = []
        task = await TasksRepository.get(task_id, session)
        task_status = task.status
        [changed_status.append(st) if st != task_status else ... for st in CompleteStatus]
        new_task = TaskSchema(status=changed_status[0], **(task.dict()))
        await TasksRepository.complete(new_task, session)

    @staticmethod
    async def delete_task(task_id, session: AsyncSession):
        await TasksRepository.delete(task_id, session)
