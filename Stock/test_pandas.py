# -*- coding: utf-8 -*-
import requests
#import numpy　
import pandas as pd
#from bs4 import BeautifulSoup
import matplotlib.pyplot as plt  ## draw tool_1
import seaborn as sns     ## draw tool_2
from matplotlib.font_manager import FontProperties

myfont=FontProperties(fname=r'C:\Users\krone.yen\Desktop\msj.ttf',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})


"""
###pandas studying 
###Series 欄位(一維度)
s1 = pd.Series([1,2,3,6,7])
s2 = pd.Series([1,2,3,6,7],index=['A','B','C','D','E'])
print(s1)
print(s2)
###DataFrame 表格（二維度）

#df = pd.DataFrame()
res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
df = pd.read_html(res.text)[0]
df_row = pd.DataFrame(df,columns=['有價證券代號及名稱',  '國際證券辨識號碼(ISIN Code) ...','CFICode','備註'])

"""


#res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")

#df = pd.read_html(res.text)[0]
df = pd.read_html('stock_data.html')[0]
#df =df.head(10)
df.columns = df.iloc[0]  ## 指定title
#print(df.columns)
df = df.iloc[1:]
#print(df.columns)
df = df.drop(columns=['國際證券辨識號碼(ISIN Code)','市場別','CFICode','備註'])
df = df.dropna(thresh=3,axis=0).dropna(thresh=3,axis=1)
df.set_index(['有價證券代號及名稱','上市日','產業別'])
df = df.sort_values(by=['上市日','產業別'],ascending=False)  ## 排序 反向
## df['產業別'].isin(['光電業'])
#df_unique = df['產業別'].unique()
## where = 光電業 ==> 產生新的dataframe
#df = df.loc[df['產業別'].isin(['半導體業'])]  ## in
#df = df[df['產業別'] == '半導體業']

## select
#print(df[['有價證券代號及名稱','產業別']].head(10))
## groupby & sum()
#df=df[df['產業別'] == '半導體業'].groupby(by='產業別')['產業別'].count()
#df_1 =df.groupby(by='產業別')['產業別'].count()

df_2_o=df.groupby(by='產業別')['產業別'].count().reset_index(name='數量') ## alias name 'counts'
#print(df_2_o,type(df_2_o))
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

### plt.plot(data_x ,data_y,) for data
### sns
df_2_o[['產業別','數量']].plot(kind='bar',x='產業別',y='數量',title='產業別 VS 數量',legend = False )
#sns.barplot(x='數量', y='產業別' ,data=df_2_o )
#sns.barplot(x=[k for k, _ in cities_counter[:10]], y=[v for _, v in cities_counter[:10]])
#sns.lmplot(x='產業別',y='數量',data=df_2_o,fit_reg=False)
####明日練習 漲跌
###更改全部中文問題

plt.title('產業別 VS 數量', fontproperties=myfont)
plt.xlabel('數量', fontproperties=myfont)
plt.ylabel('產業別', fontproperties=myfont)
plt.show()

#df = df.head(10)
#df.to_csv('top_10.csv',index=False ,header=True) ##存CSV

#df = df.dropna(how='all', axis=1).dropna(how='any')
## row (axis=0) , col (axis=1) , thresh (null 數量)

#print(df_1)
"""
print('====================================')
print(df_2)


gapminder_twn = gapminder[gapminder['country'] == 'Taiwan']
gapminder_twn[['year', 'pop']].plot(kind = 'line', x = 'year', y = 'pop', title = 'Pop vs. Year in Taiwan', legend = False)
plt.show()
"""


#print(df_unique)

#df.shape：這個 DataFrame 有幾列有幾欄
#df.columns：這個 DataFrame 的變數資訊
#df.index：這個 DataFrame 的列索引資訊
#df.info()：關於 DataFrame 的詳細資訊
#df.describe()：關於 DataFrame 各數值變數的描述統計
"""
df_list  = df['有價證券代號及名稱'].astype(str).values.tolist()  ## pandas to list of type string
for df_str in df_list :
    ddf = df_str.split()
    print(ddf[0])
    #print('============')
"""



#df = df.dropna(axis=1)  ##drop 第一行以後
#print(df)
#print(type(df_row_10))
#df_row_10 = df_row_10.iloc[2:]

#df_column=df.columns
#print(df_row_10.describe())
"""
## loc --（x_label、y_label） &&  iloc （row，columns）   &&   ix (both used)
df.columns = df.iloc[0] ##取得第0 行
df_row = pd.DataFrame(df,df.columns)
# 取的表格的資訊
print(df.head(10))
"""


"""
df = df.iloc[1:]
df = df_row.dropna(thresh=3,axis=0).dropna(thresh=3,axis=1)
df =df_row.set_index(['有價證券代號及名稱'])

print(df.sort_values(by='有價證券代號及名稱').head(10))

#print(df)
# 設定名稱
df.columns = df.iloc[0]
# 刪除第一行
df = df.iloc[1:]
df = df.dropna(thresh=3,axis=0)
# head 取前 20 row
print(df.head(20))
"""

