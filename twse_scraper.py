import requests
from bs4 import  BeautifulSoup as bs
from fake_useragent import UserAgent 

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

url = 'https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU_d?date=20230331&selectType=24&response=json&_=1680575877167'
response_twse = requests.get(url=url, headers=headers)
data = response_twse.json()
print(data['data'])
