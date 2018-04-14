# -*- coding:utf-8 -*-
import json

from country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # 原始数据包含小数
        code = get_country_code(country_name)
        if code:
            print(country_name + ': ' + str(population))
        else:
            print('ERROR - ' + country_name)
