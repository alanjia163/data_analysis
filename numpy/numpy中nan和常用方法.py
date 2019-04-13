#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import numpy as np

a = np.arange(9, dtype=float).reshape(3, 3)
a[[[1], [2]]] = np.nan
print(a)
# isnan函数
print(np.isnan(a))
a[np.isnan(a)] = 0  # 把nan替换成中值或者均值
print(a)

print(np.count_nonzero(a))

# sum()统计求和
b = np.arange(12, dtype=int).reshape(2, 6)
print(b)
print(np.sum(b, axis=0))  # 得到结果和行的形状一样
print(np.sum(b, axis=1))
# .mean()
print(b.mean())
print(b.mean(axis=0))
print(b.mean(axis=1))
# np.median()中位数
print(np.median(b, axis=0))
# .min() .max()
# .ptp()机值
print(np.ptp(b))
# .std()标注差
print(np.std(b, axis=0))
