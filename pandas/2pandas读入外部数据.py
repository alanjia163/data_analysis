#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import pandas as pd
#导入数据库工具
from pymongo import MongoClient

path = './dogNames2.csv'


#read_csv()
df = pd.read_csv(path)
print(pd.read_csv(path,nrows=10))
print(df)


#连接MongDB
client = MongoClient()#默认本地Iplocalhost和端口
collection  = client['douban'['tv1']]
data= list(collection.find())

print(data)
