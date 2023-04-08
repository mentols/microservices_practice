from abc import abstractproperty

from sqlalchemy import update, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.repository import IBaseRepository, Model


class GenericRepository(IBaseRepository):
    model: Model = abstractproperty

    def __init__(self, session: AsyncSession) -> None:
        self._db_context = session

    async def get(self, **kwargs) -> Model:
        for key, value in kwargs.items():
            query = await self._db_context.execute(
                select(self.model).where(getattr(self.model, key) == value)
            )
            return query.scalars().first()

    async def create(self, instance: Model) -> int:
        self._db_context.add(instance)
        await self._db_context.commit()
        await self._db_context.refresh(instance)
        return instance.id

    async def update(self, instance: Model):
        await self._db_context.commit()
        await self._db_context.refresh(instance)

    async def delete(self, **kwargs):
        for key, value in kwargs.items():
            query = delete(self.model).where(getattr(self.model, key) == value)
            await self._db_context.execute(query)
            await self._db_context.commit()
