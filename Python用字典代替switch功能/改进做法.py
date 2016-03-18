# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-28 11:01'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


def if1():
    print 'i am if1'

def if2():
    print 'i am if2'

def if3():
    print 'i am if3'

mydict = {'1':if1, '2':if2, '3':if3}

mydict.get('1')()

