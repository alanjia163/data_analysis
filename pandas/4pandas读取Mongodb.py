#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

from pymongo import MongoClient
import pandas as pd

client =MongoClient()

collection = client["douban"]["tv1"]
data= list(collection.find())

df = pd.DataFrame(data)
print(df)
