import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    MongoURI = os.getenv('MONGO_URI')
    Topic = os.getenv('TOPIC')
    Server = os.getenv('BOOTSTRAP_SERVER')
