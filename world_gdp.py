# -*- coding:utf-8 -*-
import json
import pygal.maps.world as pmw
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# 创建一个包含gdp的字典
cc_gdps = {}
# 打印每个国家2016年的GDP
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = float(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

# 根据gdp值将所有的国家分成三组
cc_gdps_1, cc_gdps_2, cc_gdps_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 10000000000:
        cc_gdps_1[cc] = gdp
    elif gdp < 100000000000:
        cc_gdps_2[cc] = gdp
    else:
        cc_gdps_3[cc] = gdp

# 看看每组分别包含多少个国家
# print(len(cc_gdps_1), len(cc_gdps_2), len(cc_gdps_3))

wm_style = RS('#d8886d', base_style=LCS)  # 让Pygal使用一种基色
wm = pmw.World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('0-10bn', cc_gdps_1)
wm.add('10bn-100bn', cc_gdps_2)
wm.add('>100bn', cc_gdps_3)

wm.render_to_file('diagram/Grouped_World_GDP_2016.svg')
