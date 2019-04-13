#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

from matplotlib import  pyplot as plt
import numpy as np
#设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,1,1,3,3,3,2,3,8,4,5,6,5,4,3,3,1,1,1]

y_1 =a
y_2 =b
x=range(11,31)

plt.figure(figsize=(12,5),dpi=60)

#x,y label
plt.xlabel('岁数')
plt.ylabel('朋友个数')
#x,y xticks
plt.xticks(range(11,31))
# 计算颜色值
#color = np.arctan2(y_1,x)
# 绘制散点图
#plt.scatter(x, y_1, s = 75, c = color, alpha = 0.5)

#设置柱状图
#plt.bar(x, y_1, s = 75,  facecolor = 'green', edgecolor = 'white')

#绘制图并添加标签
plt.plot(x,y_1,label='11111111自己')
plt.plot(x,y_2,label='同桌')


#绘制网格,调整虚化程度
plt.grid(alpha=0.1)

plt.show()