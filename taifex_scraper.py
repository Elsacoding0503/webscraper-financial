# 台灣期貨taifex
import requests
from bs4 import  BeautifulSoup as bs
from fake_useragent import UserAgent 

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
    'Content-Type': 'application/json;charset=UTF-8'
}

url_taifex = 'https://mis.taifex.com.tw/futures/api/getQuoteList'

json_data = {
    'MarketType': '0',
    'SymbolType': 'F',
    'KindID': '1',
    'CID': '',
    'ExpireMonth': '',
    'RowSize': '全部',
    'PageNo': '',
    'SortColumn': '',
    'AscDesc': 'A',
}

response_taifex = requests.post(url=url_taifex,headers=headers, data=json.dumps(json_data))
data_taifex = response_taifex.json()
data_taifex['RtData']['QuoteList']