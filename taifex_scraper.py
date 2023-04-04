# 證交所twse
import requests
import pandas as pd
from fake_useragent import UserAgent 

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

url = 'https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU_d?date=20230331&selectType=24&response=json&_=1680575877170'
response_twse = requests.get(url=url, headers=headers)
data_twse = response_twse.json()

code = [content_twse[0] for content_twse in data_twse['data']]
titles = [content_twse[1] for content_twse in data_twse['data']]
yield_ = [content_twse[2] for content_twse in data_twse['data']]
dividend_year = [content_twse[3] for content_twse in data_twse['data']]
pe_ratio = [content_twse[4] for content_twse in data_twse['data']]
prb = [content_twse[5] for content_twse in data_twse['data']]
financial_statement_yq = [content_twse[6] for content_twse in data_twse['data']]

semi_con = {}
semi_con["證券代號"]=code
semi_con["股票名稱"]=titles
semi_con["殖利率"]=yield_
semi_con["股利年度"]=dividend_year
semi_con["本益比"]=pe_ratio
semi_con["股價淨值比"]=prb
semi_con["財報年度年/季"]=financial_statement_yq

df_semi = pd.DataFrame(semi_con)
df_semi.to_csv("twse_semi_con.csv",encoding='utf-8', index=False)