# -*- coding:utf-8 -*-
import csv


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 创建一个与被打开文件相关联的reader对象
    header_row = next(reader)  # 返回文件中的下一行

    for index, column_header in enumerate(header_row):
        print(index, column_header)
