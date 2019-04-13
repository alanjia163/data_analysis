#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

'''
DataFrame是一个Series容器
'''

import pandas as pd
import numpy as np


#DataFrame会自动生成行和列的索引,行索引index,:axis0,列索引columns:axis=1
t = pd.DataFrame(np.arange(12).reshape(3,4))
print(t)

# shape(3,4)index = (abc),pd.DataFrame可以指定行列索引
t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('xyzs'))
print(t1)

#给DataFrame传值的两种方式,
t2 = {'name':['xiaoming','xiaohong'],'age':[16,30]}
t2 = pd.DataFrame(t2)
print(t2)

t3 = [{'name':'xiaohong','age':16},{'name':'xiaoming','age':18}]
t3 = pd.DataFrame(t3)
print(t3)

print(type(t1))
print(type(t2))
print(type(t3))

