import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta  ##月
import matplotlib.pyplot as plt  ## draw tool_1
import seaborn as sns     ## draw tool_2
from matplotlib.font_manager import FontProperties
import yfinance as yf
yf.pdr_override()


myfont=FontProperties(fname=r'C:\Users\krone.yen\Desktop\msj.ttf',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})


stock_data = input('Input Sotck ID:')
start_date = datetime.date.today() - datetime.timedelta(days=7)
#start_date = datetime.date.today() - relativedelta(month=1)
end_date = datetime.date.today()

print(start_date,end_date)
## Date             High    Low   Open  Close     Volume  Adj Close

#df_csvsave = web.DataReader('1536.TW',"yahoo",datetime.datetime(2019,7,1),datetime.date.today())
#df_stock = web.DataReader(stock_data,"yahoo",start_date,end_date)

try :
           df_stock = web.get_data_yahoo(stock_data + '.TW' , start_date,end_date)
           #df_stock = web.DataReader(stock_data + '.TW', "yahoo", start_date, end_date)
           plt.plot(df_stock.Close)
except :

           df_stock = web.get_data_yahoo(stock_data + '.TWO', start_date, end_date)
           #df_stock = web.DataReader(stock_data + '.TWO', "yahoo", start_date, end_date)
           plt.plot(df_stock.Close)


#plt.plot(df_stock.Close)
df_title = stock_data + '-'+ ' 一周股價'
plt.title(df_title,fontproperties=myfont,loc='right')
plt.xlabel('日期',fontproperties=myfont)
plt.ylabel('價格', fontproperties=myfont)
plt.show()



#print (df_csvsave)
#df_csvsave.to_csv(r'C:\Users\krone.yen\Desktop\table.csv',columns=df_csvsave.columns,index=True)


