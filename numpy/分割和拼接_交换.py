#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
import numpy as np

t1 = np.arange(12).reshape(2, 6)
print(t1)
t2 = np.arange(24).reshape(4, 6)
print(t2)

# #竖直拼接
print(np.vstack((t1, t2)))

# 水平拼接,但是此时拼接不行,对应的维度必须相同
# print(np.hstack((t1, t2)))


# 行交换,注意行列交换对应位置加上:,
t3 = np.arange(1, 10).reshape(3, 3)
t3[[1, 2], :] = t3[[2, 1], :]
print(t3)

# 列交换
t3 = np.arange(1, 10).reshape(3, 3)
t3[:, [1, 2]] = t3[:, [2, 1]]
print(t3)
