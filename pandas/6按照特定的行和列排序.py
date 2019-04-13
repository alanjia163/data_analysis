#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import pandas as pd

df = pd.read_csv("./dogNames2.csv")
# print(df.head(5))
# print('*'*100)
# print(df.info())
# print(df.describe())

# 按照特定列排序
df = df.sort_values(by='Count_AnimalName', ascending=False)
print(df.head(5))

# 切片
# 方括号写数字,表示取行,方括号写字符串,表示取列索引,对列操作
df = df[:20]  # 取行
df = df['Row_Labels']  # 取列
# 另外上面两个操作可以连着取
