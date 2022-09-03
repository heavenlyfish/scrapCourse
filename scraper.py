import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/news/world')
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('a',{'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'})

title_list =[]
for title in titles:
    title_list.append(title.getText())

print(title_list)
