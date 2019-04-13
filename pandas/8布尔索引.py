#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import pandas as pd
import numpy as np
df = pd.read_csv("./dogNames2.csv")
print((800<df['Count_AnimalName'])&(df['Count_AnimalName']<1000))

#判断是否是nan
#pd.isnull()
#pd.notnull()

#删除为nan的行货列,t1.dropna(axis=0,how='all',inplace)全部为nan的才删除,how也可以等于any
#填充为nan的地方数据,t1.fillna(0)