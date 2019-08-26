import pandas as pd
#from bs4 import BeautifulSoup
import matplotlib.pyplot as plt  ## draw tool_1
import seaborn as sns     ## draw tool_2
from matplotlib.font_manager import FontProperties

myfont=FontProperties(fname=r'C:\Users\krone.yen\Desktop\msj.ttf',size=14)
sns.set(font=myfont.get_family())
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

df = pd.read_html('stock_data.html')[0] ## in the D:\python_dir\Stock

df.columns = df.iloc[0]  ## 指定title

df = df.iloc[1:]
#print(df.columns)
df = df.drop(columns=['國際證券辨識號碼(ISIN Code)','市場別','CFICode','備註'])
df = df.dropna(thresh=3,axis=0).dropna(thresh=3,axis=1)
df.set_index(['有價證券代號及名稱','上市日','產業別'])
df = df.sort_values(by=['上市日','產業別'],ascending=False)  ## 排序 反向
df_2_o=df.groupby(by='產業別')['產業別'].count().reset_index(name='數量') ## alias name 'counts'


#print(df_2_o['產業別'],type(df_2_o))
#df_2_o[['產業別','數量']].plot(kind='bar',x='產業別',y='數量',title='產業別 VS 數量',legend = False ) ##縱向
#df_2_o[['產業別','數量']].plot(kind='barh',x='產業別',y='數量',title='產業別 VS 數量',legend = False ) ##橫向
#sns.barplot(x='數量', y='產業別' ,data=df_2_o )
data = df_2_o[ (df_2_o['產業別'] == '半導體業') | (df_2_o['產業別'] == '光電業') ]
#print(data)

plt.pie(data['數量'],labels=data['產業別'],autopct='%1.1f%%')  ## pie
#plt.pie(df_2_o['數量'],labels=df_2_o['產業別'],autopct='%1.1f%%')  ## pie

plt.title('產業別 VS 數量', fontproperties=myfont)
plt.xlabel('數量', fontproperties=myfont)
plt.ylabel('產業別', fontproperties=myfont)
plt.axis('equal')
plt.show()
