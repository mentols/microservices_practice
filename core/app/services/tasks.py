from typing import List

from fastapi import HTTPException
from starlette import status

from app.generics.uow import UnitOfWork
from app.models.tasks import Task
from app.schemas.tasks import TaskIn as TaskSchemaIn
from producer import send_one


class TasksServices:
    def __init__(self):
        self.uow = UnitOfWork()

    async def get_all_tasks(self, page_id: int) -> List[Task]:
        async with self.uow:
            return await self.uow.tasks.all(page_id=page_id)

    async def get_task(self, task_id: int) -> Task:
        async with self.uow:
            task = await self.uow.tasks.get(id=task_id)
            if task:
                return task
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task is not exists",
            )

    async def create_task(self, page_id: int, task: TaskSchemaIn) -> None:
        async with self.uow:
            task = Task(page_id=page_id, **(task.dict()))
            await self.uow.tasks.create(task)
            await send_one({'add_t': page_id})

    async def complete_task(self, task_id: int) -> None:
        async with self.uow:
            task = await self.uow.tasks.get(id=task_id)
            task.flip_status()
            await self.uow.tasks.update(task)
            await send_one({'upd': task.page_id})

    async def delete_task(self, task_id) -> None:
        async with self.uow:
            await self.uow.tasks.delete(id=task_id)
