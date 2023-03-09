from app.database.mongo import get_db as db
from app.schemas.pages import Page as PageSchema


class PagesRepository:
    @staticmethod
    async def get(page_id: int):
        client = await db()
        document = await client['pages'].find_one({"page_id": page_id})
        return document

    @staticmethod
    async def create(page: PageSchema) -> None:
        client = await db()
        await client['pages'].insert_one(page.dict())

    @staticmethod
    async def create_task(page: PageSchema) -> None:
        client = await db()
        await client['pages'].update_one({"page_id": page.page_id}, {"$set": page.dict()})

    @staticmethod
    async def update(page: PageSchema) -> None:
        client = await db()
        await client['pages'].update_one({"page_id": page.page_id}, {"$set": page.dict()})

    @staticmethod
    async def delete(page_id: int) -> None:
        client = await db()
        await client['pages'].delete_one({"page_id": page_id})
