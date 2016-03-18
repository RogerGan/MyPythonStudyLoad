# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-09-23 16:40'

__mail__ = 'chaojiang.gcj@alibaba-inc.com/393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'


import matplotlib.pyplot as plt

# data
x = [0,5,9,10,15]
y = [0,1,2,3,4]

# trick to get the axes
fig,ax = plt.subplots()

# make ticks and tick labels
xticks = range(min(x),max(x)+1,3)
xticklabels = ['2000-01-0'+str(n) for n in range(1,len(xticks)+1)]

# plot data
ax.plot(x,y)

# set ticks and tick labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels,rotation=15)

# show the figure
plt.show()