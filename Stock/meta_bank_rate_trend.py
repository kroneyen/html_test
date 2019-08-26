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


### execute python with sys argv
def check_sys_date(s_day_from , s_day_return , s_currency) :
    import sys
    today = datetime.date.today()
    end_day = today - datetime.timedelta(days=60)
    try :
          s_day_from = sys.argv[1]
          s_day_return = sys.argv[2]
          s_currency = sys.argv[3]
    except :
           print('please execute python with sys_argv {start_date , end_date , currency ,during_day}')
           sys.exit(1)

    ###   s_day_from
    if s_day_from == '0' :
       #day_from = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days = 11),'%Y/%m/%d')  ## booking friday
       day_from = end_day.strftime("%Y/%m/%d")
    else :
       day_from = s_day_from
    ### s_day_return
    if s_day_return == '0' :
       #day_return = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days = 14),'%Y/%m/%d') ## booking next monday
       day_return = today.strftime("%Y/%m/%d")

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
    else  :  ## default JPY
         currency = '08'

    return day_from , day_return , currency

start_date , end_date , currency  = check_sys_date(None,None,None)

url='https://ebank.megabank.com.tw/global2/rs/rs03/PRS3000.faces?taskID=PRS300'
downloadType='TEXT'
### currency mapping
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
     time.sleep(random.randrange(1, 2, 1))
     ##radio menu for trend
     web.find_element_by_id('main:lastRadio').click()
     time.sleep(random.randrange(1, 2, 1))
     web.find_element_by_id("main:startDate").clear()
     web.find_element_by_id("main:startDate").send_keys(start_date)
     time.sleep(random.randrange(1, 2, 1))
     web.find_element_by_id("main:endDate").clear()
     web.find_element_by_id("main:endDate").send_keys(end_date)
     ##Drop-down menu
     Select(web.find_element_by_id("main:downloadType")).select_by_value(downloadType)
     #time.sleep(random.randrange(1, 2, 1))
     ##submit
     web.find_element_by_id('main:j_id32').click() ## for trend
     time.sleep(random.randrange(3, 5, 1))

except :
     print('bank_rate id down')
### pandas process

soup = BeautifulSoup(web.page_source, "html.parser")
tables_data = []
## get all data for tables tag
for table_head in soup.find_all('table',{'class':re.compile('^table_head')}) :
    tables_data.append(table_head)

## table data split
table_head_left_du = str(tables_data[0]) ## for plot title
table_head_top_str = str(tables_data[1]) ## for plot data
### build dataframe
df1 = pd.read_html(table_head_left_du)[0]  ## read pandas for title
df = pd.read_html(table_head_top_str)[0]   ## read pandas for data
## rename columns name
df = df.dropna(axis=1, how='all')  ## axis 0:  Drop rows ,1: Dro columns
## adding  ATM price name & data  (即期賣匯 +現金賣匯 ) / 2
df['ATM中價'] = round((df[df.columns[3]]+df[df.columns[4]])/2,5)
## object to datetime for index
df['日期'] = pd.to_datetime(df['日期'])
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
df.plot(kind='line', x=df.columns[0], y=df.columns[-3:] ,title=title_list)
plt.show()

## D:\python_dir\venv\Scripts\python.exe test_bank_rate.py 0 0 USD










