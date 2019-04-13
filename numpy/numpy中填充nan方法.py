#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import numpy as np


def nan_to_mean(t1):#将t1中nan值转换成中间值
    t1[1, 2:] = np.nan
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:
            tem_not_nan_col = temp_col[temp_col == temp_col]
            temp_col[np.isnan(temp_col)] = tem_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype('float')
    print(nan_to_mean(t1))
