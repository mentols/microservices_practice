from motor.motor_asyncio import AsyncIOMotorClient

from config import Config


async def get_db() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(Config.MongoURI)
    db = client.pages
    return db
