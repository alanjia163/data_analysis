#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

'''
高性能
常见数据类型:
    Series一维,带标签数组
    DataFrame二维,Series容器
'''

import pandas as pd

p1 = pd.Series([1, 3, 6, 4, 2])
print(p1)

# 可以指定
t2 = pd.Series([1, 2, 3, 47, 4], index=list('abcde'))
print(t2)
temp_dict = {'age': 18, 'name': 'mayun', 'tel': 10086}
t3 = pd.Series(temp_dict)
print(t3)

# 通过键取值,和下标取值
print(t3['age'])
print(t3[2])

# 布尔索引
t4 = pd.Series(range(10))

print(t4[t4 > 1])

#index and values
print(t4.index)
print(t4.values)

