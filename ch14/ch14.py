#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 14:44
# @Author  : dly
# @File    : ch14.py
# @Desc    :

from utils.util import split_line

# -----------------------------------------------------------------------------------
'''
迭代器
'''


def it_test():
    s = 'ABC'
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break


# it_test()

split_line()

# -----------------------------------------------------------------------------------
'''
yield
生成器函数,返回一个生成器对象
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


s = Sentence('hello world, a b c')
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
