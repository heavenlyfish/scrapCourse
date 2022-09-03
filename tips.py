# 3.8 五個優化網頁爬蟲穩定度的技巧
# 設定HTTP Headers 標頭
# 設定 HTTP Request timeout(超時)屬性
# 檢查 爬取的元素是否存在
# 例外處理機制


import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

try:
    response = requests.get(
        'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt', 
        headers = headers, 
        timeout = 10, 
    )

    if response.status_code == 200:

        soup = BeautifulSoup(response.text,'lxml')
        titles = soup.find_all(
            'h2',{'class':'bbc-19hmebw e47bds20'}
        )
        if titles:
                
            title_list = []
            for title in titles:
                title_list.append(title.getText())
            print(title_list)
        else:
                print('元素不存在!')
    
    else:
        print('狀態碼非200!')

except Exception as e:
    print(str(e))