#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import numpy as np

t1 = np.arange(16).reshape((4,4))
print(t1)
#方法一
t1 = t1.T
print(t1)
#方法二
t1 = t1.transpose()
print(t1)
#方法三
t1 = t1.swapaxes(0,1)
print(t1)

