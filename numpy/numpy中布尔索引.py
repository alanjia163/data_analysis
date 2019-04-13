#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
import numpy as np

t = np.arange(24).reshape((4, 6))
print(t)
print(t > 20)
print(t[t > 20])
t[t > 20] = 11
print(t)

# np.where三目函数
np.where(t > 10, 3, 1)
print(t)
