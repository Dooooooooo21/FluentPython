#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 10:32
# @Author  : dly
# @File    : 07.py
# @Desc    :

def split_line():
    print('-----------------------------------------------------------------------')


def deco(func):
    def inner():
        print('inner running')

    return inner


# 使用deco 装饰target
@deco
def target():
    print('running target')


print(target())
print(target)
split_line()

# ------------------------------------------------------------------------
'''
函数装饰器以及被装饰的函数执行顺序:
函数装饰器在导入模块时立即执行
被装饰的函数只在明确调用时运行
'''
registry = []


def register(func):
    print('running register{0}'.format(func))
    registry.append(func)

    return func


@register
def f1():
    print('running f1')


@register
def f2():
    print('running f2')


def f3():
    print('running f3')


print('running start')
print('registry ', registry)
f1()
f2()
f3()
split_line()

# -----------------------------------------------------------------------
'''
字节码
'''
from dis import dis


def f5():
    print('running f5')


print(dis(f5))
split_line()

# ----------------------------------------------------------------------------
'''
闭包: 指延伸了作用域的函数
能访问定义体之外的非全局变量
'''


def make_averger():
    series = []

    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averger()
print(avg(10))
print(avg(11))
print(avg(12))
split_line()

# -------------------------------------------------------------------------------
'''
@functools.lru_cache
备忘功能，保存耗时的函数结果，避免传入相同的参数重复计算
适用于递归等
缓存的空间有限制，一段时间不用的会被丢弃
'''

# --------------------------------------------------------------------------------
'''
@functools.singledispatch
单分派泛函数
根据第一个参数的类型，以不同方式执行相同操作
'''

# --------------------------------------------------------------------------------

