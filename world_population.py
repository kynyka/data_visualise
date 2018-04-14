# -*- coding:utf-8 -*-
import json
import pygal.maps.world as pmw
from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2008':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # 原始数据包含小数
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = pmw.World()
wm.title = 'World Population in 2008, by Country'
wm.add('2008', cc_populations)

wm.render_to_file('diagram/world_population_2008.svg')
