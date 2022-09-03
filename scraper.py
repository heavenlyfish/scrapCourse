import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/news')
soup = BeautifulSoup(response.text, 'lxml')
title = soup.find('a',{'class':'bbc-uk8dsi e1d658bg0'})
print(title)