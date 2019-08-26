# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import time
import webbrowser, os

import random

## https://www.twse.com.tw/fund/TWT54U?response=html&date=20190722&selectType=ALL 法人買賣超 week (一)

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


ttoday_delt =  (datetime.date.today().weekday())
## 計算本周星期一 日期
w_date =  (datetime.date.today() - datetime.timedelta(days=ttoday_delt)).strftime("%Y%m%d")


in_str_date = input('input Monday date :')

if  len(in_str_date) > 5 and in_str_date <= w_date :
            str_date = in_str_date

elif datetime.date.today().isoweekday() == 1 :
     str_date = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y%m%d")

else :
      str_date = w_date

##https://www.twse.com.tw/fund/TWT54U?response=html&date=20190725&selectType=ALLBUT0999
url = 'https://www.twse.com.tw/fund/TWT54U?response=html&date=' + str_date + '&selectType=ALLBUT0999'
## 證券代號	證券名稱	外陸資買進股數(不含外資自營商)	外陸資賣出股數(不含外資自營商)	外陸資買賣超股數(不含外資自營商)	外資自營商買進股數	外資自營商賣出股數	外資自營商買賣超股數	投信買進股數	投信賣出股數	投信買賣超股數	自營商買賣超股數	自營商買進股數(自行買賣)	自營商賣出股數(自行買賣)	自營商買賣超股數(自行買賣)	自營商買進股數(避險)	自營商賣出股數(避險)	自營商買賣超股數(避險)	三大法人買賣超股數
##df[df.columns[2]] = (df[df.columns[2]] // 1000).map(lambda x:format (x , ','))
df = pd.read_html(url)[0]

df_title = df.columns.get_level_values(0)[0]
df.columns = df.columns.get_level_values(1)
df =df.iloc[:,[0,1,4,10,11,-1]]
df = df.rename(columns={"外陸資買賣超股數(不含外資自營商)": "外資","投信買賣超股數":"投信","自營商買賣超股數":"自營商","三大法人買賣超股數":"總數"})

print(df.info())
df[df.columns[2]] = (df[df.columns[2]] // 1000)
df[df.columns[3]] = (df[df.columns[3]] // 1000)
df[df.columns[4]] = (df[df.columns[4]] // 1000)
df[df.columns[-1]] = (df[df.columns[-1]] // 1000)
print(df.info())
#df = df.head(20)
## df.style.apply(color(), axis=1)
#dfs =df.style.applymap(color_negative_red, subset=['外資','投信','自營商','總數']).format({'外資': "{:,}"}).format({'投信': "{:,}"})
#dfs =df.style.applymap(color_negative_red, subset=['外資','投信','自營商','總數']).format({'外資': "{:,.0f}",'投信': "{:,.0f}"})
dfs =df.head(20).style.applymap(color_negative_red, subset=['外資','投信','自營商','總數']).format({'外資': "{:,}",'投信': "{:,.0f}",'自營商': "{:,.0f}",'總數': "{:,.0f}"})
#dfs =df.style.applymap(color_negative_red, subset=['外資','投信','自營商','總數']).format({'漲幅%': "{:.2%}"})

#df.style.format({'B': "{:0<4.0f}", 'D': '{:+.2f}'})
#dfs = df.style.applymap(color_negative_red,subset=['漲跌價差','漲幅%']).format({'漲幅%': "{:.2%}"}).set_table_styles(styles)
print(df.info())

dfs_style = dfs.render()

try :
      with open('Top20_3_Investors.html','w') as f:
          f.write(df_title)
          f.write(dfs_style)
finally :
      f.close()

time.sleep(random.randrange(1, 2, 1))
filename = 'file:///'+os.getcwd()+'/' + 'Top20_3_Investors.html'
webbrowser.open_new_tab(filename)
