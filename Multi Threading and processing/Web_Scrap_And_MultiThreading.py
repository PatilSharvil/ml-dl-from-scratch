# Web  Scrapping often involves making numerous requests to fetch web pages. these tasks are IO Bound because they spend a lot of time waiting for response from server. 
# Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently

# https://docs.langchain.com/oss/python/langchain/overview

# https://docs.langchain.com/oss/python/langchain/quickstart

# https://docs.langchain.com/oss/python/langchain/agents

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/oss/python/langchain/quickstart',
    'https://docs.langchain.com/oss/python/langchain/agents'
]

def fetch_content(url) : 
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(f'fetched : {len(soup.text)} charecters from url')

threads = []

for url in urls : 
    thread = threading.Thread(target=fetch_content, args= (url,))
    threads.append(thread)
    thread.start()
    
for thread in threads : 
    thread.join()
    
print('All web pages fetched')