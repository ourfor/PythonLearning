#/bin/python
#coding: utf-8
#author: ourfor
#date: 20190123
#description: 利用python的matplotlib.plotpy和numpy函数来绘制二次函数图像

#导入必要的类库
import matplotlib.pyplot as plt 
import numpy as nu 


print("绘制二次函数图像:")
#自变量取值区间-100到100,每隔0.1取一个点
x=nu.arange(-100,100,0.1)
y=x**2 + 3*x + 2

plt.title("二次函数图像")
plt.plot(x,y)
plt.show()