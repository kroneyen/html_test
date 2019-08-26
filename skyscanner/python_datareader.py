import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt  ## draw tool_1
import seaborn as sns     ## draw tool_2
#import fix_yahoo_finance as yf
#yf.pd_override()

srock_in = input("Input sotck_id :") + '.TW'
start_date = datetime.date.today() + datetime.timedelta(days=-7)
end_date = datetime.date.today()
#print(start_date ,end_date)
#df_data = web.DataReader('1536.TW',"yahoo",datetime.datetime(2019,7,1),datetime.date.today())
df_data = web.DataReader(srock_in,"yahoo",start_date,end_date)
#plt.plot(df_data.Close,'-',label="收盤價")
#plt.title(srock_in , loc='right')
df_data.Close.plot()
plt.show()

"""
fig = plt.figure(figsize=(10, 6))
plt.plot(stock_6207_2018_pd.close, '-' , label="收盤價")
plt.plot(stock_6207_2018_pd.open, '-' , label="開盤價")
plt.title('雷科股份2018 開盤/收盤價曲線',loc='right')
# loc->title的位置
plt.xlabel('日期')
plt.ylabel('收盤價')
plt.grid(True, axis='y')
plt.legend()
fig.savefig('day20_01.png')


plt.title('產業別 VS 數量', fontproperties=myfont)
plt.xlabel('數量', fontproperties=myfont)
plt.ylabel('產業別', fontproperties=myfont)
plt.show()

"""




#print (df_csvsave)
## Columns=   High    Low   Open  Close     Volume   Adj Close
#df_csvsave.Close.plot() ## columns = Close
#plt.show()

#df_csvsave.to_csv(r'C:\Users\krone.yen\Desktop\table.csv',columns=df_csvsave.columns,index=True)


