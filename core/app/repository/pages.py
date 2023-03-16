from typing import List

from sqlalchemy import select

from app.generics.repository import GenericRepository
from app.schemas.pages import Page as PageSchema
from app.models.pages import Page
# todo: contextvar
# todo: decode_access_jwt_token in services


class PagesRepository(GenericRepository):
    model = Page

    def __init__(self, session):
        self.session = session
        super().__init__(session)

    async def all(self) -> List[PageSchema]:
        result = await self.session.execute(select(Page))
        print(result)
        return result.scalars().all()
