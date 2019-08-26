# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import time
import webbrowser, os
import random

## 漲幅排行

##yahoo
## 上漲 上市/上櫃
## https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse&n=30
##https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse
## https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=otc&n=30

## 跌幅 上市/上櫃
#https://tw.stock.yahoo.com/d/i/rank.php?t=down&e=tse&n=30
#https://tw.stock.yahoo.com/d/i/rank.php?t=down&e=otc&n=30


##https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20190730&stockNo=1536



def color_negative_red(val):
  """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """

    #color = 'green' if val < 0 else 'black'

    if val < 0 :
        color = 'green'
    elif val == 0:
        color = 'black'
    else:
        color = 'red'

    return 'color: %s' % color


# Set CSS properties for th elements in dataframe
th_props = [
  ('font-size', '11px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', '#6d6d6d'),
  ('background-color', '#f7f7f9')
  ]

# Set CSS properties for td elements in dataframe
td_props = [
  ('font-size', '15px')
  ]

# Set table styles
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]



## https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse&n=30
##https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse
## https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=otc&n=30
#url_list = ['https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse&n=30','https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=otc&n=30']
url = 'https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=tse&n=30'


## 證券代號	證券名稱	外陸資買進股數(不含外資自營商)	外陸資賣出股數(不含外資自營商)	外陸資買賣超股數(不含外資自營商)	外資自營商買進股數	外資自營商賣出股數	外資自營商買賣超股數	投信買進股數	投信賣出股數	投信買賣超股數	自營商買賣超股數	自營商買進股數(自行買賣)	自營商賣出股數(自行買賣)	自營商買賣超股數(自行買賣)	自營商買進股數(避險)	自營商賣出股數(避險)	自營商買賣超股數(避險)	三大法人買賣超股數
##df_m_t[df_m_t.columns[2]] = (df_m_t[df_m_t.columns[2]] // 1000).map(lambda x:format (x , ','))
#print(url)
for url in url_list :

    df = pd.read_html(url)[1]
