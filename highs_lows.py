# -*- coding:utf-8 -*-
import csv
from datetime import datetime

from matplotlib import pyplot as plt


# 从文件中获取日期、最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与被打开文件相关联的reader对象
    header_row = next(reader)  # 返回文件中的下一行

    dates, highs, lows = [], [], []  # 注意第一行已在next()时被读取
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])  # 转成数字才能被matplotlib读取
            low = int(row[3])
        except ValueError:  # 有些气象站会偶尔出现故障,未能收集部分或全部其应该收集的数据,缺失数据可能会引发异常;这里
            print(current_date, 'missing data')  # 处理为打印错误消息,指出缺失数据的日期,并于打印后循环接着处理下一行
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 根据数据绘制图形
    fig = plt.figure(dpi=96, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # 透明度,默认1完全不透明
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签,以免彼此重叠
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='both', labelsize=16)
    # plt.gca().xaxis.set_major_locator(plt.AutoLocator())  # 设置刻度间距 MaxNLocator(14)|AutoLocator()是MaxNLocator with simple defaults. This is the default tick locator for most plotting.|LinearLocator是evenly spaced ticks from min to max

    plt.show()
