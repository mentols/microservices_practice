from typing import Generic, Type

from app.interfaces.repository import IBaseRepository, T, Collection


class GenericRepository(IBaseRepository, Generic[T]):
    def __init__(self, collection: Type[Collection]):
        self.collection = collection

    async def get(self, **kwargs) -> T:
        search_field = list(kwargs.keys())[0]
        instance_value = list(kwargs.values())[0]
        return await self.collection.find_one({search_field: instance_value})

    async def create(self, instance: T) -> None:
        await self.collection.insert_one(instance.dict())

    async def update(self, instance: T) -> None:
        """
            In non mongo database we need to use the 'id' but not 'page_id'
            It is crutch for this solution
        """
        instance_id = instance
        await self.collection.update_one({'page_id': instance_id}, {"$set": instance.dict()})

    async def delete(self, **kwargs) -> None:
        search_field = list(kwargs.keys())[0]
        instance_value = list(kwargs.values())[0]
        await self.collection.delete_one({search_field: instance_value})
