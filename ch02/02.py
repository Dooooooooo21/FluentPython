#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 15:25
# @Author  : dly
# @File    : 02.py
# @Desc    :
import os
from collections import namedtuple

lax_coordinates = (33.9, -118.4)
# 元组拆包
latitude, longitude = lax_coordinates

print(latitude)
print(longitude)

# divmod(x, y)
# Return the tuple (x//y, x%y).
print(divmod(20, 8))

# 拆分路径和文件名
print(os.path.split('/home/python/test.py'))
# ('/home/python', 'test.py')

# 用 * 来处理剩下的元素
a, b, *c = range(5)
print(a, b, c)

# 具名元组
City = namedtuple('City', 'name country population coordinates')
# 字段
print(City._fields)

tokyo = City('Tokyo', 'JP', 36.9, (35.6, 239.6))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

# 转字典
print(tokyo._asdict())

# 切片赋值
l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

l[2:5] = [100]
print(l)

# 对序列使用 + 和 *
board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'x'
print(board)

# 三个列表指向同一对象的引用
board = [['_'] * 3] * 3
print(board)

board[1][2] = '0'
print(board)

# +=
t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)
