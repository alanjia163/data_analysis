#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import numpy as np

t1 = np.arange(16).reshape((4, 4))
print(t1)

# 取行
print('*' * 15)  # 分割线***********
print(t1[[2],])
# 不连续多行,注意多一层中括号
print(t1[[2, 3], :])
# 连续多行
print(t1[2:, :])

# 取列
print('*' * 15)  # 分割线***********
print(t1[:, 2])  # 第三列
print(t1[:, 2:])  # 第三列后的每一列
print(t1[:, [1, 3]])  # 不连续多列

#同时取行和取列,会自动取交集
print('*' * 15)  # 分割线***********
print(t1[1:3,1:4])
#取不相邻的多个点
print('*' * 15)  # 分割线***********
print(t1[[1,0],[2,3]])#!!!!!!!!!!!!!(1和2)对应成为一个值,(0和3)为另外一个值
print(t1[[1],[2]])