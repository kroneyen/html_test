# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import time
import webbrowser, os
import random

### 融資融眷前30名



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


#ttoday_delt =  (datetime.date.today().weekday())
## 計算本周星期一 日期
#w_date =  (datetime.date.today() - datetime.timedelta(days=ttoday_delt)).strftime("%Y%m%d")


in_str_date = input('input date :')

if  len(in_str_date) > 5 :
            str_date = in_str_date

elif datetime.date.today().isoweekday() == 1 :
     str_date = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y%m%d")

else :
       str_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")


url = 'https://www.twse.com.tw/exchangeReport/MI_MARGN?response=html&date='+ str_date +'&selectType=ALL'
#url = '20190726.html'


## 證券代號	證券名稱	外陸資買進股數(不含外資自營商)	外陸資賣出股數(不含外資自營商)	外陸資買賣超股數(不含外資自營商)	外資自營商買進股數	外資自營商賣出股數	外資自營商買賣超股數	投信買進股數	投信賣出股數	投信買賣超股數	自營商買賣超股數	自營商買進股數(自行買賣)	自營商賣出股數(自行買賣)	自營商買賣超股數(自行買賣)	自營商買進股數(避險)	自營商賣出股數(避險)	自營商買賣超股數(避險)	三大法人買賣超股數
##df_m_t[df_m_t.columns[2]] = (df_m_t[df_m_t.columns[2]] // 1000).map(lambda x:format (x , ','))
#print(url)
df = pd.read_html(url)[1]
#print(df.head())
##  股票代號	股票名稱	買進	賣出	現金償還	前日餘額	今日餘額	限額	買進	賣出	現券償還	前日餘額	今日餘額	限額	資券互抵	註記
df_title = df.columns.get_level_values(0)[0]
df_title_1 = df.columns.get_level_values(1)[7:9]
df.columns = df.columns.get_level_values(2)
## 20190726
"""
print(df_title)
print(df_title_1)
print(df.columns )
"""
df = df.iloc[:,[0,1,2,3,4,8,9,10]]

## 逗號移除
#print(len(df.columns))

"""
for i in range(2,len(df.columns)) :
  df[df.columns[i]] = df[df.columns[i]].astype(str).apply(lambda x: x.replace(',', ''))
  #df[df.columns[i]].apply(lambda x: x.replace(',', ''))
  df[df.columns[i]] = df[df.columns[i]].astype(float)
"""
#print(df.iloc[:,2].head(10))

#df['融資進出'] = (df.iloc[:,2] - df.iloc[:,3] -  df.iloc[:,4])
df.insert(loc=2,column='融資進出',value=(df.iloc[:,2] - df.iloc[:,3] - df.iloc[:,4]))
df.insert(loc=3,column='融券進出',value=(df.iloc[:,7] - df.iloc[:,6] - df.iloc[:,8]))



"""
108年07月26日 融資融券彙總 (全部)
Index(['股票代號', '股票名稱', '買進', '賣出', '現金償還', '前日餘額', '今日餘額', '限額', '買進', '賣出',
       '現券償還', '前日餘額', '今日餘額', '限額', '資券互抵', '註記'],
      dtype='object')
"""

df = df.iloc[:,0:4]

dfs = df.sort_values(df.columns[2],ascending =False).head(30).reset_index(drop=True).style.applymap(color_negative_red, subset=['融資進出','融券進出'])
dfs_sell = df.sort_values(df.columns[3],ascending =False).head(30).reset_index(drop=True).style.applymap(color_negative_red, subset=['融資進出','融券進出'])

dfs_style = dfs.render()
dfs_sell_style = dfs_sell.render()
dfs_list = [dfs_style,dfs_sell_style]
try :
      with open('Daily_Margin_Trade_Short_Sell.html','w') as f:
          f.write(df_title)
          for i in range(len(dfs_list)) :
              if i > 0 :
                 f.write('*'*70)

              f.write(dfs_list[i])

finally :
      f.close()

time.sleep(random.randrange(1, 2, 1))
filename = 'file:///'+os.getcwd()+'/' + 'Daily_Margin_Trade_Short_Sell.html'
webbrowser.open_new_tab(filename)
