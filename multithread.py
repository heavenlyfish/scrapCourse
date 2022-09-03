from concurrent.futures.process import _MAX_WINDOWS_WORKERS
import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

def scraps(links):
    response = requests.get(links)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('h2',{'class':'bbc-19hmebw e47bds20'})

    title_list=[]
    for title in titles:
        title_list.append(title.getText())
    urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})
    for url in urls:
        sub_response = requests.get(url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
        
        tag_list = []
        for tag in tags:
            tag_list.append(tag.find('a').getText())

    print(title_list)
    print(tag_list)


start_time = time.time()

links=[f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}' for page in range(1,4) ]

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scraps,links)

end_time = time.time()

print(f'花費{end_time - start_time}秒')
