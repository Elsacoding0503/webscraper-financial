# yahoo stock
import requests
import pandas as pd
from pandas import json_normalize
from bs4 import  BeautifulSoup as bs
import json
from fake_useragent import UserAgent 

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

url_yahoo = 'https://tw.stock.yahoo.com/class-quote?sectorId=42&exchange=TAI'
response_yahoo = requests.get(url=url_yahoo, headers=headers)
soup_yahoo = bs(response_yahoo.text,'lxml')
rows = soup_yahoo.find_all('div', {'class':'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})

list_all = []
for row in rows:
    item = {}
    item["股票名稱"] = row.find('div', {'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).text
    item["股票代號"] = row.find('span', 'Fz(14px) C(#979ba7) Ell').text.split(".")[0]
    item["股價"] = row.find_all('div', {'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'})[0].text
    item["漲跌"] = row.find_all('div', {'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0].text
    item["漲跌幅"] = row.find_all('div', {'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1].text.replace("%", "")
    price_yesterday = row.find_all('div', {'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'})[2].text
    if price_yesterday > item["股價"]:
        item["漲跌"] = '-' +item["漲跌"]
        item["漲跌幅"] = '-' +item["漲跌幅"]
    list_all.append(item)

    
for offset in (30,60):
    url_detail = f'https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getClassQuotes;exchange=TAI;offset={offset};sectorId=42?bkt=&device=desktop&ecma=modern&feature=ecmaModern%2CuseNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=09o80eli2nnir&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1787&returnMeta=true'
    response_detail = requests.get(url=url_detail, headers=headers)
    
    detail = response_detail.json()
    for i in detail["data"]["list"]:
        dict_detail = {}
        dict_detail["股票名稱"]=i["symbolName"]
        dict_detail["股票代號"]=i["symbol"]
        dict_detail["股價"]=i["price"].split(".")[0]
        dict_detail["漲跌"]=i["change"].replace("+","")
        dict_detail["漲跌幅"]=i["changePercent"].replace("%", "").replace("+","")
        list_all.append(dict_detail)
        
with open ('上市光電.json', 'w') as f:
        json.dump(list_all, f, indent=4, ensure_ascii=False)

# dict_all = {}
# dict_all["results"] = list_all
# data_all = json.dumps(dict_all, ensure_ascii=False)
# df = json_normalize(dict_all["results"])
