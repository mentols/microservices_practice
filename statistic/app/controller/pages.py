from fastapi import HTTPException
from starlette import status

from app.repository.pages import PagesRepository
from app.schemas.pages import Page as PageSchema


class PagesController:
    def __init__(self, client):
        self.repository = PagesRepository(client)

    async def control(self, message: dict):
        key: str = [k for k in message][0]
        value: int = [v for v in message.values()][0]
        action_dict = {
            'add': self.create_page,
            'upd': self.update_page,
            'del': self.delete_page,
            'add_t': self.create_task
        }
        await action_dict.get(key)(value)

    async def statistic(self, page_id: int):
        page_statistic = await self.repository.get(page_id=page_id)
        if page_statistic:
            return page_statistic
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Page is not exists",
        )

    async def create_page(self, page_id: int):
        page = PageSchema(
            page_id=page_id,
            task_amount=0,
            resolved=0,
            unresolved=0,
            resolution_percentage=0,
        )
        await self.repository.create(page)

    async def create_task(self, page_id: int):
        page = await self.repository.get(page_id=page_id)
        page.unresolved += 1
        page.task_amount += 1
        page.resolution_percentage = await self.calculate_resolution_percentage(
            page.resolved, page.task_amount
        )
        await self.repository.create_task(page)

    async def update_page(self, page_id: int):
        old_page = await self.repository.get(instance_id=page_id)
        old_page.unresolved -= 1
        old_page.resolved += 1
        new_page = PageSchema(
            page_id=page_id,
            task_amount=old_page.task_amount,
            resolved=old_page.resolved,
            unresolved=old_page.unresolved,
            resolution_percentage=await self.calculate_resolution_percentage(
                old_page.resolved, old_page.task_amount
            ),
        )
        await self.repository.update(new_page)

    async def delete_page(self, page_id: int):
        await self.repository.delete(page_id=page_id)

    async def calculate_resolution_percentage(self, resolved: int, amount: int):
        return round((resolved / amount) * 100, 2)
