from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import async_session
from app.interfaces.uow import IUnitOfWork
from app.repository.pages import PagesRepository
from app.repository.tasks import TasksRepository


class UnitOfWork(IUnitOfWork):
    def __init__(self, session_factory=async_session):
        self.session_factory = session_factory
        self._session = None

    async def __aenter__(self) -> AsyncSession:
        self._session: AsyncSession = self.session_factory()
        self.pages = PagesRepository(self._session)
        self.tasks = TasksRepository(self._session)
        return self._session
        # async with async_session() as session:
        #     yield session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        await self._session.close()
        self._session = None

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
