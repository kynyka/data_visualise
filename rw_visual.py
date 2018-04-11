# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 只要程序处于活动状态,就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw = RandomWalk(50000)  # 将类默认的5000点增多指50000点
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=96, figsize=(10, 6))  # 系统分辨率,Py默认80dot/inch|屏幕分辨率>放大或缩小文本和其他项目>设置自定义文本大小

    point_numbers = list(xrange(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = raw_input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
