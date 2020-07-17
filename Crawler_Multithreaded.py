"""
Multithreaded approach
"""
from multiprocessing import Process
import time
from urllib.request import urlopen
from threading import Thread


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.dawn.com')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.twitter.com')
    # add other urls
    return urls_list


def crawl_one_url(url):
    html = urlopen(url)
    text = html.read()


if __name__ == "__main__":

    urls_to_crawl = get_urls_to_crawl()
    start = time.time()

    threads = list()
    for url in get_urls_to_crawl():
        threads.append(Thread(target=crawl_one_url, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))

