"""
SUBSCRIBE TO REDIS PUBSUB as a generator
"""

import aioredis
import asyncio
from collections import deque
from statistics import mean

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
        yield int(msg)


async def subscribe3():
    """
    print average of all seen numbers
    """
    n = 0
    s = 0
    async for msg in subscribe2():
        n += 1
        s += msg
        print(f"Average of {n} numbers is {s/n:.3f}")


async def subscribe4(n=10):
    """
    moving average of last 10 numbers in the channel
    """
    data = deque(maxlen=n)
    async for msg in subscribe2():
        data.append(msg)
        m = mean(data)
        print(f"Average of last {len(data)} numbers is {m:.3f}")


async def subscribe5():
    """
    squares, filters above 60 and maintains average of last 10, compare with only average of last 10
    """
    data1 = deque(maxlen=10)
    data2 = deque(maxlen=10)
    async for msg in subscribe2():
        data2.append(msg)
        msg_sq = msg*msg
        if msg_sq >= 60:
            data1.append(msg_sq)
        print(f"Average of last {len(data1)} squares above 60 is {mean(data1)} and generic average is {mean(data2)}")
    


if __name__=='__main__':
    asyncio.run(subscribe5())


