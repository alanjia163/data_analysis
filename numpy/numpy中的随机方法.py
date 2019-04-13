#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
import numpy as np

t1 = np.arange(1, 13).reshape(3, 4)
print(t1)
print(t1.shape)
# zeros((shape),dtype)
add_one = np.zeros((t1.shape[1]), dtype=int)
print(add_one)
add_two = np.ones((t1.shape[0], 1), dtype=int)
print(add_two)

t3 = np.vstack((t1, add_one))
t4 = np.hstack((t1, add_two))
print(t1)
print('33333333333333')
print(t3)
print('444444444444')
print(t4)
# 最大值最小值/最大值所在的行/列的下标
print(np.argmax(t4))
print(np.argmax(t4, 0))  # 返回没一行最大值 所在的列
print(np.argmax(t4, 1))  # 返回没一列最大值 所在的行

# 返回最大/最小下标
print(t4.argmax())
print(t4.argmin())


t5 = np.random.randint(1,10,(3,3))
print(t5)

print('777777')
np.random.seed(12)#种子值不必设定,如果想重新运行程序随机数相同则指定种子值
t6 = np.random.randint(1,10,(3,3))
print(t6)
t7 = np.random.randint(1,10,(3,3))
print(t7)