import json

from aiokafka import AIOKafkaProducer
from app.config import Config


# todo: add login
async def send_one(message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=Config.Server)
    await producer.start()
    try:
        await producer.send_and_wait(Config.Topic, json.dumps(message).encode('utf-8'))
    finally:
        await producer.stop()
