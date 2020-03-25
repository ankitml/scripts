import asyncio
import aiohttp

URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{}.json"


async def fetch_numberof_comments(session, post_id):
    url = URL_TEMPLATE.format(post_id)
    async with session.get(url) as response:
        response_text = await response.json()
        if 'kids' not in response_text:
            return 0
        kids = response_text['kids']
        number_of_comments = len(kids)
        tasks = [fetch_numberof_comments(session, kid_id)
                 for kid_id in kids]
        kid_results = await asyncio.gather(*tasks)
        number_of_comments += sum(kid_results)
        print(f'POST id {post_id} has {len(kids)} no of kids')
        return number_of_comments


async def main(post_id):
    async with aiohttp.ClientSession() as session:
        result = await fetch_numberof_comments(session, post_id)
        return result


if __name__ == '__main__':
    post_id = 22683750
    results = asyncio.run(main(post_id))
    print(f'Number of comments - {results}')
