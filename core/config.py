import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    User = os.getenv("DB_USER")
    Password = os.getenv("DB_PASSWORD")
    Name = os.getenv("DB_NAME")
    Host = os.getenv("DB_HOST")
    Port = os.getenv("DB_PORT")
    Config = f"postgresql+asyncpg://{User}:{Password}@{Host}:{Port}/{Name}"

    Server = os.getenv("BOOTSTRAP_SERVER")
    Topic = os.getenv("TOPIC")

