#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 22:47
# @Author  : dly
# @File    : 03.py
# @Desc    :

import collections
from types import MappingProxyType

ct = collections.Counter('abcabcddd')
print(ct)

d = {1: 'A'}
# 不可变映射类型
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])

# TypeError: 'mappingproxy' object does not support item assignment
# d_proxy[2] = 'B'
# print(d_proxy)

d[2] = 'B'
print(d_proxy)


# 字典和集合 速度非常快
