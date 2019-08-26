# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt  ## draw tool_1
import seaborn as sns     ## draw tool_2
from matplotlib.font_manager import FontProperties
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import calendar
from bs4 import BeautifulSoup
import time
import random
import re

### chinese module
myfont=FontProperties(fname=r'C:\Users\krone.yen\Desktop\msj.ttf',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

### cmd line :
### execute python with sys argv
def check_sys_date(s_day_from , s_day_return , s_currency) :
    import sys
    ## datetime prepare
    today = datetime.date.today()
    end_day = today - datetime.timedelta(days=60)
    try :
          s_day_from = sys.argv[1]
          s_day_return = sys.argv[2]
          s_currency = sys.argv[3]
    except :
           print('please execute python with sys_argv')
           sys.exit(1)

    ###   s_day_from
    if s_day_from == '0' :
       #day_from = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days = 11),'%Y/%m/%d')  ## booking friday
       day_from = today.strftime("%Y/%m/%d")
    else :
       day_from = s_day_from
    ### s_day_return
    if s_day_return == '0' :
       #day_return = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days = 14),'%Y/%m/%d') ## booking next monday
       day_return = end_day.strftime("%Y/%m/%d")
    else :
       day_return = s_day_return
    ###    s_currency
    if  s_currency == 'USD' :
        currency = '01'
    elif s_currency == 'EUR' :
         currency = '37'
    elif s_currency == 'GBP' :
         currency = '04'
    elif s_currency == 'AUD' :
         currency = '05'
    else :  ## default JPY
         currency = '08'

    return day_from , day_return , currency

start_date , end_date , currency  = check_sys_date(None,None,None)

url='https://ebank.megabank.com.tw/global2/rs/rs03/PRS3000.faces?taskID=PRS300'
#bank_rate_JPY ='D:\python_dir\Stock\test_bank_rate.html'
#url = 'test_bank_rate.html'

downloadType='TEXT'

""" 
        <option value="01">美金[USD]</option>
        <option value="03">港幣[HKD]</option>
        <option value="04">英鎊[GBP]</option>
        <option value="05">澳幣[AUD]</option>
        <option value="06">新加坡幣[SGD]</option>
        <option value="07">瑞士法郎[CHF]</option>
        <option value="08">日圓[JPY]</option>
        <option value="09">加拿大幣[CAD]</option>
        <option value="12">瑞典幣[SEK]</option>
        <option value="13">韓幣[KRW]</option>
        <option value="14">馬來幣[MYR]</option>
        <option value="15">印尼幣[IDR]</option>
        <option value="17">泰幣[THB]</option>
        <option value="21">菲律賓幣[PHP]</option>
        <option value="24">紐西蘭幣[NZD]</option>
        <option value="27">南非幣[ZAR]</option>
        <option value="28">澳門幣[MOP]</option>
        <option value="37">歐元[EUR]</option>
        <option value="38">越南幣[VND]</option>
        <option value="39">人民幣[CNY]</option>
"""

############## login

web = webdriver.Chrome('D:\python_dir\chromedriver')  ## for cron path
web.get(url)
time.sleep(random.randrange(3, 5, 1))


### get bank_rate info
try :
     ##Drop-down menu
     Select(web.find_element_by_id("main:currency")).select_by_value(currency)
     #time.sleep(random.randrange(1, 2, 1))
     ##radio menu
     ### 每日匯率
     web.find_element_by_id('main:dailyChangeRadio').click() ##  營業時間及非營業時間所有變動(限查詢指定日)
     #time.sleep(random.randrange(1, 2, 1))
     web.find_element_by_id("main:startDate").clear()
     web.find_element_by_id("main:startDate").send_keys(start_date)
     ##Drop-down menu
     Select(web.find_element_by_id("main:downloadType")).select_by_value(downloadType)
     #time.sleep(random.randrange(1, 2, 1))
     ##submit
     web.find_element_by_id('main:j_id31').click() ## 查詢
     #web.find_element_by_id('main:j_id32').click() ## 走勢圖
     time.sleep(random.randrange(3, 5, 1))
except :
     print('bank_rate form is failed ')


num =1
### rate page change for daily
while 1:
          btn_cls_get = web.find_element_by_id('__pagerNextj_id49').get_attribute('class')  ##查詢
          if  btn_cls_get == 'btn_2' :
               WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.ID, "__pagerNextj_id49"))).click()
               time.sleep(random.randrange(2, 3, 1))
               #soup = BeautifulSoup(web.page_source, "html.parser")
               #table_head_top = soup.find('table',class_='table_head_top')
               soup = BeautifulSoup(web.page_source, "html.parser")
               tables_data = []
               ## get all data for tables tag
               for table_head in soup.find_all('table', {'class': re.compile('^table_head')}):
                   tables_data.append(table_head)

               table_data_str = str(tables_data)
               #table_head_left_du = str(tables_data[0])  ## for plot title
               #table_head_top_str = str(tables_data[1])  ## for plot data

               if num == 1 :
                            df = pd.read_html(table_data_str)[0]
                            df = df.replace(regex={None: ''}).dropna(how='any')  ## replace NaN title
                            df.columns = df.iloc[0]
                            df = df.iloc[1:]
                            df_data = pd.read_html(table_data_str)[1].iloc[:, 1:]
                            df_data = df_data.dropna(axis=1, how='all')  ## axis 0:  Drop rows ,1: Dro columns
                            df_data['ATM中價'] = round((df_data[df_data.columns[2]] + df_data[df_data.columns[3]]) / 2, 5)

               # df_data = pd.read_html('test_bank_rate.html')[1]
               else :
                     df_data1 = pd.read_html(table_data_str)[1].iloc[:, 1:]
                     df_data1 = df_data1.dropna(axis=1, how='all')  ## axis 0:  Drop rows ,1: Dro columns
                     df_data1['ATM中價'] = round((df_data1[df_data1.columns[2]] + df_data1[df_data1.columns[3]]) / 2, 5)
                     df_data = df_data.append(df_data1, ignore_index=True)
                     #df_data = df_data.append(pd.read_html(table_head_top_str)[1].iloc[:, 1:], ignore_index=True)
                     # df_data= df_data.reset_index()
                     df_data = df_data.replace(regex={None: ''}).dropna(how='any')  ## replace NaN data

               num += 1

          else :
                print('page num end :',num)
                break

time.sleep(random.randrange(3, 5, 1))
web.quit()
#print('df:',df)
#print('df_data:',df_data)
_min = df_data.min()
_max = df_data.max()
title_list = df.to_string(index=False) ## remove index tag
#df2 = pd.concat([_min,_max],axis =0)
df2 = pd.concat([_min,_max],axis =1)
#df2 = df2.rename(columns={'       0':'min','       1':'max'})

#df2_index = df2.index.tolist()

#df2.plot(kind='line', x=df2_index, y=df2.values,title=title_list)
#plt.show()


#print('df_data_count :', len(df_data))
#print(df_data.head(10))
## ATM中價 min , max  ,df.columns[-1:] = columns name
#print(df_data.columns[-1:] , '_min:' , df_data[df_data.columns[-1:]].min())
#print(df_data.columns[-1:] , '_max:' , df_data[df_data.columns[-1:]].max())
#print('df_data:',df_data)
#title_list = df.to_string(index=False)  ## title
#_min = df_data[df_data.columns[:]].min()
#_max = df_data[df_data.columns[:]].max()
#_index = df_data.columns[0:]
#print('_min:',_min)
#print('_max:',_max)
#print('_index:',_index)
#df_2.columns = df_data.columns[0:]
#data_tuples = list(zip(_min,_max))
#print('data_tuples:',data_tuples)
#print('data_tuples:',data_tuples)
#df_2 = pd.DataFrame( data_tuples ,columns=_index)
#print('df_2:',df_2)
#df_2.plot(kind='line', y =df_2.columns[0:], title=title_list)
#plt.show()


### draw plot
#title_list = df.to_string(index=False) ## remove index tag
#df_data.plot(kind='line', y=df_data.columns[-2:] ,title=title_list)
#df_data.plot(kind='line', y=df_data.columns[-2:] ,title=title_list)
#plt.show()

## D:\python_dir\venv\Scripts\python.exe test_avg_bank_rate.py 0 0 JPY
### stop coding on 20190529





"""
               #print(table_head_top)
               table_head_top_str= str(table_head_top)
               df = pd.read_html(table_head_top_str)[0]
               df = df.dropna(axis=1, how='all')  ## 去除列 NaN
               columns_list =df.columns[1:]
               #df.plot(kind='line',x='日期',y = columns_list )
               #df.plot(kind='bar', x='日期', y=columns_list)
               #plt.show()

              # for trs in  soup.find_all('tr') :
              #     for tds in trs.find_all('td',class_='con_td')
              #     print('tds:',tds.text)

               #tables = pd.read_html(tds)[0]
               #print('table:',tables)
          else :
                 break

          ## next page
          num += 1
          time.sleep(random.randrange(5, 10, 1))
#soup_ptoken = BeautifulSoup(web.page_source, "html.parser")
#time.sleep(random.randrange(5, 10, 1))


### pandas process
df = pd.read_html('test_bank_rate.html')[0]
df = df.replace(regex={None:''}).dropna(how='any') ## replace NaN title
df.columns = df.iloc[0]
df = df.iloc[1:]

#df_data = pd.read_html('test_bank_rate.html')[1]
df_data = pd.read_html('test_bank_rate.html')[1].iloc[:,1:]
df_data1 = pd.read_html('test_bank_rate.html')[1].iloc[:,1:]
df_data = df_data.append(df_data1,ignore_index =True)
#df_data= df_data.reset_index()
df_data = df_data.replace(regex={None:''}).dropna(how='any') ## replace NaN data

#print(df.to_string(index=False))
print(df.to_string())
print('                ')
#print(df_data.head(10).to_string(index=False))
#print(df_data.to_string(index=False))
print(df_data.head(10).to_string())
#print('append_len_data:',len(df_data))
#soup = BeautifulSoup(web.page_source, "html.parser")
#soup = BeautifulSoup(test_bank_rate.html, "html.parser")

### test bank_rate.jpy html
## table_head_left_du
#table_head_left_du = soup.find('table', class_='table_head_left_du')
#able_head_top = soup.find('table', class_='table_head_top')
"""
"""
tables_data = []
## get all table data
for table_head in soup.find_all('table',{'class':re.compile('^table_head')}) :
    tables_data.append(table_head)
print('tables_data:',tables_data)
## table data split
table_head_left_du = str(tables_data[0])
table_head_top_str = str(tables_data[1])
#df = pd.read_html('test_bank_rate.html')[0]
### build dataframe
df1 = pd.read_html(table_head_left_du)[0]  ## head top
df = pd.read_html(table_head_top_str)[0]   ## rate data
## rename columns name
df = df.rename(columns={'Unnamed: 5':'ATM中價'})
## adding  ATM price  (即期賣匯 +現金賣匯 ) / 2
df['ATM中價'] = round((df[df.columns[3]]+df[df.columns[4]])/2,5)
## object to datetime for index
#df['日期'] = pd.to_datetime(df['日期'])

df1 = df1.replace({None:''},regex=True).dropna(how='any') ## remove NaN
df1.columns = df1.iloc[0]  ## 指定 index
df1 = df1.iloc[1:]   ## 指定 data
#df1 = pd.DataFrame(columns=df1.iloc[0],data=df1.iloc[0:]) ## reset columns & data
title_list = df1.to_string(index=False) ## remove index tag
#df = df.dropna(axis=1, how='all')  ## 去除列 NaN
time.sleep(random.randrange(3, 5, 1))
web.quit()
# df.plot(kind='line',x='日期',y = columns_list )
### 日期    即期買匯    現金買匯    即期賣匯    現金賣匯   ATM中價
#df.plot(kind='line', x=df.columns[0], y=df.columns[-2:] ,title=title_list)
df.plot(kind='line', y=df.columns[-2:] ,title=title_list)
plt.show()

## D:\python_dir\venv\Scripts\python.exe test_bank_rate.py 0 0 USD
"""









