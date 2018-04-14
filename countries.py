# -*- coding:utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES  # 现i18n模块不再属于pygal中

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])