# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-07-02 13:49'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


import base64
s = '我是字符串'
a = base64.b64encode(s)
print a
print base64.b64decode(a)