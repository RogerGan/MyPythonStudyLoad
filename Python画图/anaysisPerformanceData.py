# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-09-14 16:00'

import ConfigParser
import db_factory
import datetime
import sys
import matplotlib.pyplot as plt

def drawLaunchPerformanceData(buildid, filenamememory, filenametime):
    dbfactory = db_factory.get_db_connection_debug()
    conn = dbfactory.get_connection()
    cur = conn.cursor()
    sql = 'select * from ios_ninegame_performance_launch_records where buildid={}'.format(buildid)

    cur.execute(sql)
    data = cur.fetchall()
    for i in range(len(data)):
        print data
    launchdata = data[0][-1].split('&')
    memSizeBeforeLaunching = launchdata[0].split('=')[-1]
    memSizeBeforeFinishLaunching = launchdata[1].split('=')[-1]
    memSizeAfterFinishLaunching = launchdata[2].split('=')[-1]
    timeIntervalBeforeFinishLaunching = launchdata[3].split('=')[-1]
    timeIntervalAfterFinishLaunching = launchdata[4].split('=')[-1]
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
    plt.figure(1) # 创建图表1
    plt.xlabel('LaunchPerformance')
    plt.ylabel('MemoryData')
    plt.title("LaunchPerformanceData")
    plt.xticks((0,1,2),(u'memSizeBeforeLaunching',u'memSizeBeforeFinishLaunching',u'memSizeAfterFinishLaunching'))
    rect = plt.bar(left = (0,1,2),height = (float(memSizeBeforeLaunching),float(memSizeBeforeFinishLaunching),float(memSizeAfterFinishLaunching)),width = 0.35,align="center")

    # plt.legend((rect,),(u"Data",))
    autolabel(rect)
    plt.gcf().autofmt_xdate()
    plt.savefig(filenamememory, dpi = 200)
    plt.figure(2)
    plt.xlabel('LaunchPerformance')
    plt.ylabel('TimeData')
    plt.title("LaunchPerformanceData")
    plt.xticks((0,1),(u'timeIntervalBeforeFinishLaunching',u'timeIntervalAfterFinishLaunching'))
    rect = plt.bar(left = (0,1),height = (float(timeIntervalBeforeFinishLaunching),float(timeIntervalAfterFinishLaunching)),width = 0.35,align="center")
    autolabel(rect)
    plt.gcf().autofmt_xdate()
    plt.savefig(filenametime, dpi = 200)
    # plt.show()

def drawPerformance2():
    x = []
    y = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    sqlparam=ConfigParser.ConfigParser().read('sqlconfig.ini')
    dbfactory = db_factory.get_db_connection_debug()
    conn = dbfactory.get_connection()
    cur = conn.cursor()
    # sql = 'select duringtime from ios_ninegame_performance_records where buildid = {}'.format(buildid)
    sql = 'select triggertime from ios_ninegame_performance_records'
    # sql2 = 'select performancedata from ios_ninegame_performance_records where buildid = {}'.format(buildid)
    sql2 = 'select performancedata from ios_ninegame_performance_records'

    cur.execute(sql)
    data = cur.fetchall()
    # print data
    for i in range(len(data)):
        # print list(data[i])[0]
        #         y.append(datetime.datetime.strptime(str(list(data2[i])[0]).split('=')[-1], "%Y-%b-%d %H:%M"))

        x.append(datetime.datetime.strptime(list(data[i])[0], "%Y-%m-%d %H:%M:%S"))
    # print x

    cur.execute(sql2)
    data2 = cur.fetchall()
    # print data2
    for i in range(len(data2)):
        y.append(str(list(data2[i])[0]).split('=')[-1])
        # y2.append(str(list(data2[i])[0]).split('&')[-2].split('=')[-1])
        # y3.append(str(list(data2[i])[0]).split('&')[-3].split('=')[-1])
        # y4.append(str(list(data2[i])[0]).split('&')[-4].split('=')[-1])
        # y5.append(str(list(data2[i])[0]).split('&')[-5].split('=')[-1])
    conn.commit()
    cur.close()
    conn.close()
    print x
    print y
    # print y2
    plt.plot(x, y)
    plt.show()
    # plt.figure(1) # 创建图表1
    # # ax1 = plt.subplot(211) # 在图表2中创建子图1
    # # ax2 = plt.subplot(212) # 在图表2中创建子图2
    #
    # plt.plot(x, y2, label="$CPU$", color="yellow", linewidth=4)
    # plt.plot(x, y3, label="$CPUUsed$", color="red", linewidth=4)
    # plt.legend()
    # plt.savefig('CPU.png', dpi = 75)
    #
    #
    # plt.figure(2)
    # # plt.plot(x, y2, label="MemerySize", color="blue", linewidth=3)
    # plt.plot(x, y4, label="TotalSize", color="blue", linewidth=3)
    # # plt.sca(ax1)
    # plt.plot(x, y, label="CurMemery", color="yellow", linewidth=1)
    # # plt.sca(ax2)
    # plt.plot(x, y5, label="availableMem", color="green", linewidth=2)
    # plt.legend()
    # plt.savefig('Memory.png', dpi = 75)
    # # plt.show()



def drawPerformance(buildid):
    x = []
    y = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    sqlparam=ConfigParser.ConfigParser().read('sqlconfig.ini')
    dbfactory = db_factory.get_db_connection_debug()
    conn = dbfactory.get_connection()
    cur = conn.cursor()
    sql = 'select triggertime from ios_ninegame_performance_records where buildid = {}'.format(buildid)
    # sql = 'select duringtime from ios_ninegame_performance_records'
    sql2 = 'select performancedata from ios_ninegame_performance_records where buildid = {}'.format(buildid)
    # sql2 = 'select performancedata from ios_ninegame_performance_records'

    cur.execute(sql)
    data = cur.fetchall()
    # print data
    for i in range(len(data)):
        # print list(data[i])[0]
        x.append(datetime.datetime.strptime(list(data[i])[0], "%Y-%m-%d %H:%M:%S"))
    # print x

    cur.execute(sql2)
    data2 = cur.fetchall()
    # print data2
    for i in range(len(data2)):
        y.append(str(list(data2[i])[0]).split('=')[-1])
        y2.append(str(list(data2[i])[0]).split('&')[-2].split('=')[-1])
        y3.append(str(list(data2[i])[0]).split('&')[-3].split('=')[-1])
        y4.append(str(list(data2[i])[0]).split('&')[-4].split('=')[-1])
        y5.append(str(list(data2[i])[0]).split('&')[-5].split('=')[-1])
    conn.commit()
    cur.close()
    conn.close()
    print x
    print y
    print y2

    plt.figure(3) # 创建图表1
    # ax1 = plt.subplot(211) # 在图表2中创建子图1
    # ax2 = plt.subplot(212) # 在图表2中创建子图2

    plt.plot(x, y2, label="$CPU$", color="yellow", linewidth=1)
    plt.plot(x, y3, label="$CPUUsed$", color="red", linewidth=1)
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.savefig('CPU.png', dpi = 75)


    plt.figure(4)
    # plt.plot(x, y2, label="MemerySize", color="blue", linewidth=3)
    plt.plot(x, y4, label="TotalSize", color="blue", linewidth=1)
    # plt.sca(ax1)
    plt.plot(x, y, label="CurMemery", color="yellow", linewidth=1)
    # plt.sca(ax2)
    plt.plot(x, y5, label="availableMem", color="green", linewidth=1)
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.savefig('Memory.png', dpi = 75)
    # plt.show()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        buildid = sys.argv[1]
        drawPerformance(buildid)
        drawLaunchPerformanceData(buildid,'LaunchMemory.png', 'LaunchTime.png')
    pass