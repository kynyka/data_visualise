# -*- coding:utf-8 -*-
import csv

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与被打开文件相关联的reader对象
    header_row = next(reader)  # 返回文件中的下一行

    highs = []  # 注意第一行已在next()时被读取
    for row in reader:
        high = int(row[1])  # 转成数字才能被matplotlib读取
        highs.append(high)

    print(highs)
