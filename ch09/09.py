#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 21:57
# @Author  : dly
# @File    : 09.py
# @Desc    :

class Vector2d:
    # __slots__ 仅在有数百万个实例的时候使用
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        # __x, __y 私有
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)

print(set([v1, v2]))
print(hash(v1))
print(hash(v2))

print(v1.__dict__)

