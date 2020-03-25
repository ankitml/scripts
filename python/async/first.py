import asyncio
import aiohttp

URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{}.json"


async def main(post_id):
    await asyncio.sleep(1)
    return 5


if __name__ == '__main__':
    post_id = 22683750
    results = asyncio.run(main(post_id))
    print(f'RESULTS - {results}')
