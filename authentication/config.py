import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # todo: rename as 'Secret_key' and add comments
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')
    JWT_ACCESS_TTL = int(os.getenv('JWT_ACCESS_TTL'))
    JWT_REFRESH_TTL = int(os.getenv('JWT_ACCESS_TTL'))
