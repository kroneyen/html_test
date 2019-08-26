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



url='http://www.yuantaetfs.com/#/FundWeights/1066'

#df = pd.read_html(url)


web = webdriver.Chrome('D:\python_dir\chromedriver')  ## for cron path
web.get(url)
time.sleep(random.randrange(3, 5, 1))

## //*[@id="allpcf"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/div[1]/table

soup = BeautifulSoup(web.page_source,"html.parser")
#soup = BeautifulSoup(open('0050.html',encoding="utf-8"), "html.parser")
table_form = soup.find('table',id='allpcf')
table_title = table_form.find('td',class_='Table_MainTitle ng-binding').text
table_data = table_form.find_all('table',class_='tab-border')[1]
table_data_str = str(table_data)
df = pd.read_html(table_data_str)[1] ## must be string
df.columns =df.iloc[0]  ## re-define columns
df = pd.DataFrame(columns=df.iloc[0], data=df.iloc[1:,0:])  ##re-define data iloc[row,columns]
df[df.columns[2]] = df[df.columns[2]].astype(float)


print(df.sort_values(by=df.columns[0],ascending=True))  ## sort by columns[2] desc 持股權重(%)
print('*' * 50 )


print(df.sort_values(by=df.columns[2],ascending=False))  ## sort by columns[2] desc 持股權重(%)
print('*' * 50 )
df[df.columns[3]] = df[df.columns[3]].astype(int)

print(df.sort_values(by=df.columns[3],ascending=False))  ## sort by columns[2] desc股數

time.sleep(random.randrange(3, 5, 1))
web.quit()
