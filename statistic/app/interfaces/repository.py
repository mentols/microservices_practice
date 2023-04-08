from abc import ABC, abstractmethod

from typing import Generic, TypeVar

T = TypeVar('T')
Collection = TypeVar('Collection')


class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get(self, **kwargs) -> T:
        raise NotImplementedError

    @abstractmethod
    async def create(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs) -> None:
        raise NotImplementedError
