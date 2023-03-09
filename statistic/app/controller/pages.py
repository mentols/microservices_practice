from app.repository.pages import PagesRepository
from app.schemas.pages import Page


class PagesController:
    @staticmethod
    async def calculate_resolution_percentage(resolved: int, amount: int):
        return round((resolved / amount) * 100, 2)

    @staticmethod
    async def control(message: dict):
        key, value = [k for k in message], [v for v in message.values()]
        action_dict = {
            'add': PagesController.create_page,
            'upd': PagesController.update_page,
            'del': PagesController.delete_page,
            'add_t': PagesController.create_task
        }
        await action_dict.get(key[0])(value[0])

    @staticmethod
    async def statistic(page_id: int):
        page_statistic = await PagesRepository.get(page_id)
        return page_statistic

    @staticmethod
    async def create_page(page_id: int):
        page = Page(
            page_id=page_id,
            task_amount=0,
            resolved=0,
            unresolved=0,
            resolution_percentage=0,
        )
        await PagesRepository.create(page)

    @staticmethod
    async def create_task(page_id: int):
        page = await PagesRepository.get(page_id)
        page.unresolved += 1
        page.task_amount += 1
        page.resolution_percentage = await PagesController.calculate_resolution_percentage(
            page.resolved, page.task_amount
        )
        await PagesRepository.create_task(page)

    @staticmethod
    async def update_page(page_id: int):
        old_page = await PagesRepository.get(page_id)
        old_page.unresolved -= 1
        old_page.resolved += 1
        new_page = Page(
            page_id=page_id,
            task_amount=old_page.task_amount,
            resolved=old_page.resolved,
            unresolved=old_page.unresolved,
            resolution_percentage=await PagesController.calculate_resolution_percentage(
                old_page.resolved, old_page.task_amount
            ),
        )
        await PagesRepository.update(new_page)

    @staticmethod
    async def delete_page(page_id: int):
        await PagesRepository.delete(page_id)
