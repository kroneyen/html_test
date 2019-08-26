#-*- coding: utf-8 -*-

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.figure(figsize=(6,6))


x = [1,2,3,4,5,6,7,8]
y = ['一','二','C','D','E','F','G','H']
#for i in x:
#   y.append(-(i*i)+i+3)


plt.plot(x, y)
plt.title(u'测试程序', fontproperties=font)
plt.xlabel(u'x轴', fontproperties=font)
plt.ylabel(u'y轴', fontproperties=font)
plt.grid(True)
plt.show()



