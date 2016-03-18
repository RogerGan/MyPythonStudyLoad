# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-09-15 18:02'

__mail__ = 'chaojiang.gcj@alibaba-inc.com/393037282@qq.com'

__weibo__ = 'http://weibo.com/ganchaojiang'

#memSizeBeforeLaunching=44974080&memSizeBeforeFinishLaunching=109735936&memSizeAfterFinishLaunching=109834240
# &timeIntervalBeforeFinishLaunching=1.6&timeIntervalAfterFinishLaunching=1.6
import matplotlib.pyplot as plt

def drawLaunchPerformanceData(buildid, filename):
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))

    plt.xlabel('LaunchPerformance')
    plt.ylabel('Data')


    plt.title("LaunchPerformanceData")
    plt.xticks((0,1,2),(u'memSizeBeforeLaunching',u'memSizeBeforeFinishLaunching',u'memSizeAfterFinishLaunching'))
    rect = plt.bar(left = (0,1,2),height = (44974080,109735936,109834240),width = 0.35,align="center")
    # plt.legend((rect,),(u"Data",))
    autolabel(rect)
    plt.gcf().autofmt_xdate()
    plt.savefig(filename, dpi = 200)
    plt.show()
