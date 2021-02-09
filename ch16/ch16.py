#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 16:46
# @Author  : dly
# @File    : ch16.py
# @Desc    :

from utils.util import split_line

# -----------------------------------------------------------------------------------
'''
yield
生产者-消费者，协程
'''


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
