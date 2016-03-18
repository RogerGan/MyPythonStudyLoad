# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-28 11:20'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


def f(x, *args, **kwargs):
    print x
    print args
    print kwargs

f(1,2,3,4,5,y=10,z=11)
'''
    result:
            1
            (2, 3, 4, 5)
            {'y': 10, 'z': 11}
'''