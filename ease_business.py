# -*- coding:utf-8 -*-
import csv
import pygal.maps.world as pmw
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code


# 从文件中获取2017年(第62列)的国家名及其指数值
filename = 'API_IC.BUS.EASE.XQ_DS2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    some_row = ''
    for i in xrange(5):
        some_row = next(reader)
    # print some_row  # 返回第5行; 此时已遍历至第5行,故下面直接循环余下的

    eodb = {}
    for row in reader:
        country = row[0]
        code = get_country_code(country)
        if code and row[61]:  # 有的指数是空白
            index = float(row[61])
            eodb[code] = index

# 根据eodb数值,将之划分5组
eodb_1, eodb_2, eodb_3, eodb_4, eodb_5 = {}, {}, {}, {}, {}
for code, index in eodb.items():
    if index < 61:
        eodb_1[code] = index
    elif index < 101:
        eodb_2[code] = index
    elif index < 151:
        eodb_3[code] = index
    elif index < 171:
        eodb_4[code] = index
    else:
        eodb_5[code] = index

wm_style = RS('#ff7f50', base_style=LCS)
wm = pmw.World(style=wm_style)
wm.title = 'Ease of doing business index, by Country\n(1 = most business-friendly regulations)'
wm.add('0-60', eodb_1)
wm.add('61-100', eodb_2)
wm.add('101-150', eodb_3)
wm.add('151-170', eodb_4)
wm.add('>170', eodb_5)

wm.render_to_file('diagram/Ease_Business_Index_2017.svg')
