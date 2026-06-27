import threading as th
import requests
from bs4 import BeautifulSoup

urls = [
    'https://leetcode.com/u/uk8530/',
    'https://tutedude.com/category/cybersecurity',
    'https://takeuforward.org/system-design/complete-system-design-roadmap-with-videos-for-sdes'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(f'Fetched {len(soup.text)} chars from{url}')


threads = []

for url in urls:
    thread = th.Thread(target = fetch_content, args = (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("All Pages Fetched")


