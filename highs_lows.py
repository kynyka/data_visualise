# -*- coding:utf-8 -*-
import csv
from datetime import datetime

from matplotlib import pyplot as plt


# 从文件中获取日期、最高气温和最低气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与被打开文件相关联的reader对象
    header_row = next(reader)  # 返回文件中的下一行

    dates, highs, lows = [], [], []  # 注意第一行已在next()时被读取
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])  # 转成数字才能被matplotlib读取
        highs.append(high)

        low = int(row[3])
        lows.append(low)
    # 根据数据绘制图形
    fig = plt.figure(dpi=96, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # 设置图形的格式
    plt.title('Daily high and low temperatures - 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签,以免彼此重叠
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
