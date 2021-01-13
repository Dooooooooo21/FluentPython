#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 22:15
# @Author  : dly
# @File    : 05.py
# @Desc    :

# 函数是对象
def factorial(n):
    ''':returns n!'''

    return 1 if n < 2 else n * factorial(n - 1)


print(factorial.__doc__)
print(type(factorial))

fruits = ['strawbarry', 'apple', 'bear', 'fig', 'banana', 'cherry']


# 高阶函数: 接受函数作为参数，或者把函数作为结果返回的函数
def reverse(word):
    return word[::-1]


print(reverse('testing'))

print(sorted(fruits, key=reverse))
