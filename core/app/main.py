from fastapi import FastAPI

from app.database.db import init_db
from app.routers.pages import api_router as pages_router
from app.routers.tasks import api_router as tasks_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(pages_router)
app.include_router(tasks_router)
