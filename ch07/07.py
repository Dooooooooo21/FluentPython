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
