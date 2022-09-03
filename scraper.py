import grequests
from bs4 import BeautifulSoup
import time

start_time = time.time()

links = [ f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}' for page in range(1,4)]
 
reqs = (grequests.get(link) for link in links)
resps = grequests.imap(reqs, grequests.Pool(3))
for index, resp in enumerate(resps):
    
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = soup.find_all('h2',{'class':'bbc-19hmebw e47bds20'})

    title_list=[]
    for title in titles:
        title_list.append(title.getText())

    urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})
    sub_links = [url.get('href') for url in urls]
    sub_reqs = (grequests.get(sub_link) for sub_link in sub_links)    
    sub_resps =grequests.imap(sub_reqs,grequests.Pool(10))    
    
    tag_list = []
    for sub_resp in sub_resps:
        sub_soup = BeautifulSoup(sub_resp.text, 'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'}) 
        for tag in tags:
            tag_list.append(tag.find('a').getText())

    print(f"第{index+1}頁")
    print(title_list)
    print(tag_list)

end_time = time.time()


print(f"花費{end_time - start_time}秒")