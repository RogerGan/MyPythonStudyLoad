# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-09-14 15:44'

__mail__ = 'chaojiang.gcj@alibaba-inc.com/393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)
# y = [1,2,34,5,6]
# z = [3,4,523,24,3]
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
