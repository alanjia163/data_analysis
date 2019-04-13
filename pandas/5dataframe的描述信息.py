#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
基础属性
df.shape#行列
df.dtypes列数据类型
df.ndim#数据维度
df.index #行索引
df.columns#列索引
df.values#对象

#正题情况查询
df.head(3)#显示头部几行,默认5行
df.tail(3)#显示末尾几行,默认5行

df.info()#相关信息概况
df.describe()中位数等等统计
'''

from pymongo import MongoClient
import pandas as pd

client = MongoClient()

collection = client["douban"]["tv1"]
data = collection.find()

# 筛选一些想要的和不想要的信息
data_list = []

for i in data:
    # 格式 [{},{}]
    temp = []
    temp["info"] = i["info"]
    temp["rating_value"] = i["rating"]["value"]
