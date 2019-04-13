#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
from matplotlib import pyplot as plt
import matplotlib

# font = {'family': 'MicroSotf YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc('font',**font)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）




plt.figure(figsize=(20,8),dpi=200)
x = range(2,26,2)
y = [5,2,3,5,5,6,6,6,3,4,6,5]
plt.xticks(range(4,22,3))
plt.plot(x,y)
plt.savefig('./ze_fig.png')
plt.show()