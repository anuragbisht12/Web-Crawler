
"""
Generator based coroutines
"""

import aiohttp
import asyncio
import time
from urllib.request import urlopen


@asyncio.coroutine
def crawl_one_url(url, session):
    get_request = session.get(url)

    res = yield from get_request
    txt = yield from res.text()

    get_request.close()
    return txt


@asyncio.coroutine
def crawl_urls(urls_to_crawl):
    session = aiohttp.ClientSession()

    work_to_do = list()
    for url in urls_to_crawl:
        work_to_do.append(crawl_one_url(url, session))

    completed, pending = yield from asyncio.wait(work_to_do, return_when=asyncio.ALL_COMPLETED)

    # uncomment to retrieve the downloaded HTML
    # for task in completed:
    #     print(task.result())

    # remember to clean up
    yield from session.close()


def main():
    urls_to_crawl = get_urls_to_crawl()
    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawl_urls(urls_to_crawl))
    elapsed = time.time() - start
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.dawn.com')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.twitter.com')

    return urls_list


if __name__ == '__main__':
    main()

