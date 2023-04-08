from app.generics.generic import GenericRepository
from app.schemas.pages import Page as PageSchema


class PagesRepository(GenericRepository):
    def __init__(self, client):
        self.client = client
        self.collection = self.client.pages
        super().__init__(collection=self.collection)

    async def create_task(self, page: PageSchema) -> None:
        await self.collection.update_one({"page_id": page.page_id}, {"$set": page.dict()})
