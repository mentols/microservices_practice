from abc import ABC, abstractmethod

from typing import TypeVar

from app.models.base import Base

Model = TypeVar('Model', bound=Base)


class IBaseRepository(ABC):
    @abstractmethod
    async def get(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, entity):
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError
