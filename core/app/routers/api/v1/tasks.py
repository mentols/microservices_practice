from typing import List

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.schemas.tasks import Task as TaskSchema
from app.schemas.tasks import TaskIn as TaskSchemaIn
from app.services.tasks import TasksServices


class TaskRouter:
    def __init__(self):
        self.api_router = APIRouter()
        self._register_routes()
        self.service = TasksServices()

    def _register_routes(self):
        @self.api_router.get('', response_model=List[TaskSchema])
        async def get_all_tasks(page_id: int):
            tasks = await self.service.get_all_tasks(page_id)
            return tasks

        @self.api_router.post('')
        async def create_task(page_id: int, task: TaskSchemaIn):
            await self.service.create_task(page_id, task)
            return Response(status_code=status.HTTP_200_OK)

        @self.api_router.get('/{task_id}', response_model=TaskSchema)
        async def get_task(task_id: int):
            task = await self.service.get_task(task_id)
            return task

        @self.api_router.patch('/{task_id}')
        async def complete_task(task_id: int):
            await self.service.complete_task(task_id)
            return Response(status_code=status.HTTP_200_OK)

        @self.api_router.delete('/{task_id}')
        async def delete_task(task_id: int):
            await self.service.delete_task(task_id)
            return Response(status_code=status.HTTP_200_OK)
