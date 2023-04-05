import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Microservice configuration
    User = os.getenv("DB_USER")
    Password = os.getenv("DB_PASSWORD")
    Name = os.getenv("DB_NAME")
    Host = os.getenv("DB_HOST")
    Port = os.getenv("DB_PORT")
    Config = f"postgresql+asyncpg://{User}:{Password}@{Host}:{Port}/{Name}"

    # Kafka configuration
    Server = os.getenv("BOOTSTRAP_SERVER")
    Topic = os.getenv("TOPIC")

    # JWT configuration
    Secret_key = os.getenv('SECRET_KEY')
    Algorithm = os.getenv('ALGORITHM')
    JWT_Access_Ttl = os.getenv('JWT_ACCESS_TTL')
    JWT_Refresh_Ttl = os.getenv('JWT_REFRESH_TTL')
