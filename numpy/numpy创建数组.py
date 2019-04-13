#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
import random

import numpy as np

# 利用numpy创建数组的三种方法
a = np.array([1, 2, 3, ])
b = np.array(range(4, 7))
c = np.arange(7, 10)
print(a, b, c)
l = [1]
# 数据的类名
print(type(a))
# 数据的类型,所存放的数据类型,dtype是属性
print(a.dtype)
print(b.dtype)
print(c.dtype)

# c.astype调整数据类型
a.astype('int32')

# numpy中的小数,生成10个随机小数
d = np.array([random.random() for i in range(10)])
print(d)
print(d.dtype)

# 取小数
d = np.round(d, 2)
print(d)
