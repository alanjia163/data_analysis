#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
获取Rating分布情况
1.选择图形,直方图
2.准备数据
'''
import pandas as pd
from matplotlib import  pyplot as plt

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

print(df.head(3))
print(df.info())
runtime_data = df["Runtime (Minutes)"].values
max_runtime_data=runtime_data.max()
min_runtime_data=runtime_data.min()

#计算组数
num_bin = (max_runtime_data-min_runtime_data)//5

plt.figure(figsize=(15,8),dpi=80)
plt.hist(runtime_data,num_bin)
plt.xticks(range(min_runtime_data,max_runtime_data+5,5))
plt.show()
