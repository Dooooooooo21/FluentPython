#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 13:27
# @Author  : dly
# @File    : PythonCard.py
# @Desc    :

import collections
from random import choices, choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 13 张牌
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 四种花色
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 生成所有牌
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()
# 实际调用 deck.__len__()
print(len(deck))
print(deck.__len__())

# 实际调用 deck.__getitem__(0)
print(deck[0])
print(deck.__getitem__(0))

# 随机抽牌
print(choice(deck))
print(choices(deck, k=5))

# 格式化字符串
print('%f' % 1.11)

print('{0:f}{1}'.format(20, ' hello world'))
