# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-07-02 15:00'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'
import base64
import datetime

starttime = datetime.datetime.now()
f1 = open('aaa.txt', 'r')
f2 = open('bbb.txt', 'w')
base64.encode(f1, f2)
f1.close()
f2.close()
f2 = open('bbb.txt', 'r')
f3 = open('ccc.txt', 'w')
base64.decode(f2, f3)
f2.close()
f3.close()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
