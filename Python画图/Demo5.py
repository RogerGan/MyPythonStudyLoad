# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-09-14 15:44'

__mail__ = 'chaojiang.gcj@alibaba-inc.com/393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'


import numpy as np
import matplotlib.pyplot as plt

# x = range(-4, 5)
# x = range(0,4)
x = ['1','2','3','4']
# y = [elem**2 for elem in x]
# y = range(1,5)
y = [2,3,4,5]
plt.plot(x, y)
plt.legend()
plt.show()
