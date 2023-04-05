import asyncio
import logging
from time import sleep

from fastapi import FastAPI

from app.database.db import init_db
from app.routers.api.routers import v1_router
from app.config import Config

app = FastAPI()
logging.basicConfig(level=logging.WARNING)

@app.on_event("startup")
async def on_startup():
    print(f';\n\n\n\nLOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host};\n\n\n\n')
    logging.warning(f'LOGG: DB Url {Config.DatabaseUrl}\nDB Host {Config.Host}')
    sleep(5)
    await init_db()


app.include_router(v1_router)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
