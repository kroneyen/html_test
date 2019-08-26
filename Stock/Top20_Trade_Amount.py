# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import time
import webbrowser, os
import random
import threading
## URL https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX20.html  交易量top20
## https://www.twse.com.tw/exchangeReport/MI_INDEX20?response=html&date=20190723

## https://www.twse.com.tw/fund/T86?response=html&date=20190724&selectType=ALL  法人買賣超_daily
## https://www.twse.com.tw/fund/TWT54U?response=html&date=20190722&selectType=ALL 法人買賣超 week (一)
## https://www.twse.com.tw/fund/TWT54U?response=html&date=20190715&selectType=ALL
##url = 'https://www.twse.com.tw/exchangeReport/TWTASU?response=html&date=' + str_date
## https://www.twse.com.tw/exchangeReport/TWTASU?response=html&date=20190723 融券dialy


##2019/07/25
## 排名	證券代號	證券名稱	成交股數	成交筆數	開盤價	最高價	最低價	收盤價	漲跌(+/-)	漲跌價差	最後揭示買價	最後揭示賣價
## 1	00637L	元大滬深300正2	190,356,334	13,363	17.81	18.04	17.71	17.95	+	0.10	17.95	17.96

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    #color = 'red' if val < 0 else 'black'
    if val < 0 :
        color = 'green'
    elif val == 0:
        color = 'black'
    else:
        color = 'red'

    return 'color: %s' % color

"""
def input_date() :

    str_date = input('input date :')
    return str_date

   # 添加一個 thread

thd = threading.Thread(target=input_date)
thd.start()
time.sleep(4)

if len(wait_input_date) > 1:
    str_date = str(wait_input_date)
else:
    str_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")

#str_date = input_date()

"""
str_date = input('input date :')

if  len(str_date) > 1 :
    str_date = str(str_date)

elif datetime.date.today().isoweekday() == 1 :
     str_date = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y%m%d")

else :
        str_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")



url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX20?response=html&date=' + str_date

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



df = pd.read_html(url)[0]
#df = pd.read_html('Top20_Trade_Amount_1.html')[0]

df =df.iloc[:,[1,2,3,5,8,9,10]]
#df.columns[2] ='成交張數'
df = df.rename(columns={"成交股數": "成交張數"})
#df[df.columns[2]] = (df[df.columns[2]] / 1000).map(lambda x:format (x , '')) ## 成交張數
#df[df.columns[2]] = (df[df.columns[2]] // 1000).round().map(lambda x:format (x , ','))  ## 成交張數
df[df.columns[2]] = (df[df.columns[2]] // 1000).map(lambda x:format (x , ','))  ## 成交張數
df[df.columns[-1]] =  (df[df.columns[4]] - df[df.columns[3]])  ## 重新計算


#new_m = df[['108年07月24日成交量前二十名證券']].columns.remove_unused_levels()
#print(df.columns)
df_title = df.columns.get_level_values(0)[0]
df.columns = df.columns.get_level_values(1) ##  remove mutiple index[0]
#df['漲幅%'] = ((df[df.columns[4]] - df[df.columns[3]])/df[df.columns[3]]).map(lambda x:format (x , '.2%'))
df['漲幅%'] = ((df[df.columns[4]] - df[df.columns[3]])/df[df.columns[3]])
##證券代號', '證券名稱', '成交張數', '開盤價', '收盤價', '漲跌(+/-)', '漲跌價差', '漲幅%'
df = df.iloc[:,[0,1,2,3,4,6,7]]

#dfs = df.style.applymap(color_negative_red_1,subset=pd.IndexSlice[:,['漲幅%']])
#dfs = df.style.applymap(color_negative_red,subset=['漲跌價差','漲幅%']).format({'漲幅%': "{:.2%}"})
dfs = df.style.applymap(color_negative_red,subset=['漲跌價差','漲幅%']).format({'漲幅%': "{:.2%}"}).set_table_styles(styles)

dfs_style = dfs.render()

try :
      with open('Top20_Trade_Amount.html','w') as f:
         f.write(df_title)
         f.write(dfs_style)
finally :
      f.close()

time.sleep(random.randrange(1, 2, 1))
filename = 'file:///'+os.getcwd()+'/' + 'Top20_Trade_Amount.html'
webbrowser.open_new_tab(filename)
