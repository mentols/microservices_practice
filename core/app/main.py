from fastapi import FastAPI

from app.database.db import init_db
from app.routers.api.routers import v1_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(v1_router)
