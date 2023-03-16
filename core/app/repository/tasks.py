from typing import List

from sqlalchemy.future import select

from app.generics.repository import GenericRepository
from app.models.tasks import Task
from app.schemas.tasks import Task as TaskSchema


class TasksRepository(GenericRepository):
    model = Task

    def __init__(self, session):
        self.session = session
        super().__init__(session)

    async def all(self, page_id: int) -> List[TaskSchema]:
        result = await self.session.execute(select(Task).where(Task.page_id == page_id))
        return result.scalars().all()
