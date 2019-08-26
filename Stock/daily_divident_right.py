# -*- coding: utf-8 -*-
import pandas as pd
import datetime
import time

## 108年07月22日
def trans_date(sttr_list):
    trans_date = ''
    str_split_list = ''
    for sttr in sttr_list:
        row_str_split = sttr.split('年')  ## 108   年07月22日
        trans_date = str(int(row_str_split[0]) + 1911) + '/'
        ##str_split_list.append(row_str_split[0] + '/')
        row_str_split_2 = row_str_split[1].split('月') ## 07  月22日
        ## str_split_list.append(row_str_split_2[0])
        trans_date += row_str_split_2[0] + '/'
        row_str_split_3 = row_str_split_2[1].split('日')   ## 22日
        #str_split_list.append(row_str_split_3[0])
        trans_date += row_str_split_3[0]

    return trans_date

##2019/07/25
def input_date_trans(sttr_date):
    input_date = ''
    row_str_split = sttr_date.split('/')
    input_date = str(int(row_str_split[0]) - 1911) +'年'+row_str_split[1] + '月' + row_str_split[2] + '日'

    return input_date


input_date = input('input date :')

## https://stock-ai.com/twStockDiv

#df = pd.read_html('ex_d.html')[0] ## must be string

df = pd.read_html('https://www.twse.com.tw/exchangeReport/TWT48U?response=html')[0] ## must be string')[0] ## must be string

##df = pd.read_html('https://fund.bot.com.tw/z/ze/zeb/zeb.djhtm')[0] ## must be string')[0] ## must be string

#df = pd.read_html('https://histock.tw/stock/dividend.aspx')[0] ## must be string


#str_date =input_date_trans(input_date)
#print(str_date)

## 日期 股票代號     名稱       現金股利     股價  現金殖利率%
df = df.iloc[:,[0,1,2,7,11]]  ## fileter columns data
df[df.columns[3]] = df[df.columns[3]].astype(float) ## 轉型態 for sort
df = df.rename(columns={df.columns[4]: "股價"})
#df['現金殖利率%'] = (df[df.columns[3]] / df[df.columns[4]]).map(lambda x:format (x , '.2%'))   ## 現金股利 / 股價 %
df['現金殖利率%'] = (df[df.columns[3]] / df[df.columns[4]]).map(lambda x:format (x , '.2%'))   ## 現金股利 / 股價 %

#df[df.columns[5]] = df[df.columns[5]].astype(float)## 轉型態 for sort

try :
        str_date = input_date_trans(input_date)
        ff = df[df.columns[0]] == str_date


except :
       ##取的今天
       yy =  str(int(datetime.date.today().strftime("%Y")) - 1911) + '年'
       ff = df[df.columns[0]] == time.strftime('{y}%m{m}%d{d}').format(y=yy,m='月',d='日')  ## where condition current day
       #ff = df[df.columns[0]] == time.strftime('{y}%m{m}%d{d}').format(y= str(int(datetime.date.today().strftime("%Y")) - 1911) + '年', m='月',d='日')  ## where condition current day
       dd = time.strftime('{y}%m{m}%d{d}').format(y=yy, m='月', d='日')

df = df.where(ff).dropna()  ## for where

df_cash_divid = df.sort_values(df.columns[3],ascending =False).iloc[:,1:].reset_index(drop=True)
df['yield'] =(df[df.columns[3]] / df[df.columns[4]]).map(lambda x:format (x , '.4'))## 轉型態 for sort

df_cash_divid_yield = df.sort_values(df.columns[6],ascending =False).iloc[:,1:-1].reset_index(drop=True)


if len(input_date) >0 :
    str_date = str_date
else :
    str_date = dd

## to html
df_cash_divid.to_html('df_cash_divid.html')
df_cash_divid_yield.to_html('df_cash_divid_yield.html')
"""
print('現金股利 ')
print(df_cash_divid)
print('*' * 50)
print('現金殖利率%')
print(df_cash_divid_yield)
"""
