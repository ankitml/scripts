"""
SIMPLE PERIODIC PUBLISHING TO REDIS
"""

import aioredis
import asyncio
import random


CHANNEL = "first"

async def publish1():
    """
    Publish a random number every second
    """
    redis = await aioredis.create_redis('redis://localhost')
    while True:
        await asyncio.sleep(1)
        r = random.randint(1, 100)
        print(f'PUBLISHING MESSAGE {r}')
        await redis.publish(CHANNEL, r)


if __name__=='__main__':
    asyncio.run(publish1())
