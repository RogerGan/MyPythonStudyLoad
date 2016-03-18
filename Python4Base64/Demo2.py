# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-07-05 17:18'

__mail__ = '393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'

import base64
f = open('client_error.log', 'r')
f2 = open('eee.txt', 'w')
base64.decode(f, f2)
f.close()
f2.close()