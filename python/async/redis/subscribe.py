"""
SUBSCRIBE TO REDIS PUBSUB as a generator
"""

import aioredis
import asyncio

CHANNEL = "first"

async def subscribe1():
    """
    subscribe to a channel and print its events
    """
    redis = await aioredis.create_redis('redis://localhost')
    channel = await redis.subscribe(CHANNEL)
    channel = channel[0]
    while True:
        await channel.wait_message()
        msg = await channel.get(encoding='utf-8')
        print(msg)


async def subscribe2():
    """
    subscribe to a channel, yield values that can be used over async for
    """
    redis = await aioredis.create_redis('redis://localhost')
    channel = await redis.subscribe(CHANNEL)
    channel = channel[0]
    while True:
        await channel.wait_message()
        msg = await channel.get(encoding='utf-8')
        yield msg

async def main():
    async for msg in subscribe2():
        print(msg)


if __name__=='__main__':

    asyncio.run(main())


