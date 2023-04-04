# 台灣期貨taifex
import requests
import pandas as pd
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

futures_domestic = {}
futures_domestic["商品"] = [i["DispCName"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["買進"] = [i["CBestBidPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["買量"] = [i["CBestBidSize"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["賣出"] = [i["CBestAskPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["賣量"] = [i["CBestAskSize"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["成交價"] = [i["CLastPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["漲跌"] = [i["CDiff"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["振幅％"] = [i["CAmpRate"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["成交量"] = [i["CTotalVolume"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["開盤"] = [i["COpenPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["最高"] = [i["CHighPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["最低"] = [i["CLowPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["參考價"] = [i["CRefPrice"] for i in data_taifex['RtData']['QuoteList']]
futures_domestic["時間"] = [i["CDate"] for i in data_taifex['RtData']['QuoteList']]

df_future_dom = pd.DataFrame(futures_domestic)
df_future_dom.to_csv("futures_domestic.csv",encoding='utf-8', index=False)