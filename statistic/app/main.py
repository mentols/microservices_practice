from fastapi import FastAPI

# from app.database.utils import connect_to_mongo, close_mongo_connection
from app.routers.api.routers import v1_router

app = FastAPI()


# @app.on_event("startup")
# async def start():
#     await connect_to_mongo()
#
#
# @app.on_event("shutdown")
# async def stop():
#     await close_mongo_connection()


app.include_router(v1_router)
