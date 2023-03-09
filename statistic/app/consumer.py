import asyncio
import logging
import sys

from aiokafka import AIOKafkaConsumer

from app.controller.pages import PagesController
from app.serializers.pages import serializer
from config import Config


async def consume():
    consumer = AIOKafkaConsumer(
        Config.Topic,
        bootstrap_servers=Config.Server,
        value_deserializer=serializer
    )
    try:
        await consumer.start()
        async for msg in consumer:
            data_string = f"Consumed! Topic: {msg.topic}, Partition: {msg.partition}, Offset: {msg.offset}, " \
                          f"Key: {msg.key}, Value: {msg.value}, Timestamp: {msg.timestamp}"
            logging.basicConfig(level=data_string)
            await PagesController.control(msg.value)
    except KeyboardInterrupt:
        await consumer.stop()


if __name__ == '__main__':
    try:
        asyncio.run(consume())
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
