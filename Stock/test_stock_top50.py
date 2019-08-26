# -*- coding: utf-8 -*-
#import requests
import pandas as pd
#import matplotlib.pyplot as plt  ## draw tool_1
#import seaborn as sns     ## draw tool_2
#from matplotlib.font_manager import FontProperties

#myfont=FontProperties(fname=r'C:\Users\krone.yen\Desktop\msj.ttf',size=14)
#sns.set(font=myfont.get_family())
#sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

#df = pd.read_html('top_50.html')[0]
df = pd.read_html('http://money-104.com/download/paper_t05st09sub_boa_20190222.html')[0]
df.columns = df.iloc[0]  ## 指定title
df = pd.DataFrame(columns=df.columns[1:],data=df.iloc[1:])  ## all data
## P/E Ratio
#df = df.replace({'-':None},regex=True).dropna(how='any') ## 去除null 跟 '-'
df = df.replace(regex={'^-*$':None}).dropna(how='any') ## 去除null 跟 '-'
#df = df.replace({'0.00%':None}).dropna() ## 去除null 跟 '0.00%'
df[df.columns[-2]] = df[df.columns[-2]].astype(float)  ## 轉換數值 (本益比)
df[df.columns[6]] = df[df.columns[6]].astype(float).round(4)  ## 轉換數值 (現 金股利及股票股利合計)
df[df.columns[7]] = df[df.columns[7]].astype(float)  ## 轉換數值 (股價)
df[df.columns[-3]] = df[df.columns[-3]].str.rstrip('%').astype(float)  ## 轉換數值 (現金+股票股利殖利率)
#print(df['最新本益比(2019-03-29)'])
pe_ratio = df.sort_values(by=[df.columns[-2]],ascending=True).where(df[df.columns[6]] >0 ).dropna().iloc[1:51]  ## top 50 sort:最新本益比(2019-03-29)
pe_ratio_top_50 = pd.DataFrame(columns=pe_ratio.columns[[0,1,6,7,-2]],data=pe_ratio) ## 重整資料
#print(pe_ratio_top_50)

## 現金+股票股利殖利率
d_y = df.sort_values(by=[df.columns[-3]],ascending=False).iloc[1:101]  ## top 50 sort: 現金+股票股利殖利率
d_y_top_50 = pd.DataFrame(columns=d_y.columns[[0,1,6,7,-3]],data=d_y) ## 重整資料
#d_y_top_50.columns=['股票代號','股票名稱','股利及股息合計','前日收盤價','殖利率'] ## 更換title
#print(d_y_top_50)

##EPS
#eps = df.sort_values(by=[df.columns[6],df.columns[7]],ascending=False).iloc[1:61]  ## top 50 sort: 現金+股票股利殖利率
#eps = df.sort_values(by=[df.columns[6],df.columns[7]],ascending=False).where(df[df.columns[7]] < 300).dropna().iloc[1:101]  ## top 50 sort: 現 金股利及股票股利合計 && 股價小於300
dividends = df.sort_values(by=[df.columns[6],df.columns[7]],ascending=False).dropna().iloc[1:101]  ## top 100 sort: 現 金股利及股票股利合計 && 股價小於300
#eps_columns=eps.columns[[0,1]]
dividends_top_100 = pd.DataFrame(columns=dividends.columns[[0,1,6,7]],data=dividends) ## 重整資料
#eps_top_100.columns=['股票代號','股票名稱','股利及股息合計','前日收盤價'] ## 更換title
#eps_top_100 = pd.DataFrame(columns=['股票代號','股票名稱','股利及股息合計','前日收盤價'],data=eps) ## 重整資料
#eps_top_50 = pd.DataFrame(columns=eps_columns,data=eps) ## 重整資料
print('==========  股利合計 Top100 股價  ========')
#print(eps_top_100.to_string(index=False))
print(dividends_top_100.to_html(index=False))
print('========= 現金+股票股利殖利率 Top50 ========')
#print(d_y_top_50.to_string(index=False))
print(d_y_top_50.to_html(index=False))
print('========= 本益比 Top50 ========')
#print(pe_ratio_top_50.to_string(index=False))
print(pe_ratio_top_50.to_html(index=False))
#print(eps_top_50)




