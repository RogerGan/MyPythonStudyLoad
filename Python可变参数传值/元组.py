# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-28 11:19'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


def f(x, *args):
    print x
    print args
f(1,2,3,4,5)
'''
    :return
    1
    (2, 3, 4, 5)
'''