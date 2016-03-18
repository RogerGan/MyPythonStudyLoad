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

def getmethod(opera):
    if opera == '1':
        if1()
    elif opera == '2':
        if2()
    elif opera == '3':
        if3()
    else:
        print 'error'

getmethod('2')

# 效率底下，因为如果是‘3’的话要做3次判断才拿到结果