from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.models.base import Base
from app.config import Config

print(f';\n\n\n\nLOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host};\n\n\n\n')

engine = create_async_engine(Config.DatabaseUrl, echo=True, future=True)
async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
print(f';\n\n\n\nLOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host};\n\n\n\n')


# todo: add writes in log
async def init_db():
    print(f';\n\n\n\nLOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host};\n\n\n\n')
    async with engine.begin() as conn:
        print(f';\n\n\n\nLOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host};\n\n\n\n')
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
