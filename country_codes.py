# -*- coding:utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    '''根据指定的国家,返回Pygal使用的两个字母的国别码'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif name == 'Egypt, Arab Rep.':
            return 'eg'
        elif name == 'Gambia, The':
            return 'gm'
        elif name == 'Hong Kong SAR, China':
            return 'hk'
        elif name == 'Iran, Islamic Rep.':
            return 'ir'
        elif name == 'Kyrgyz Republic':
            return 'kg'
        elif name == 'Lao PDR':
            return 'la'
        elif name == 'Slovak Republic':
            return 'sk'
        elif name == 'Tanzania':
            return 'tz'
        elif name == 'Vietnam':
            return 'vn'
        elif name == 'Yemen, Rep.':
            return 'ye'
    # 如果没有找到指定的国家,就返回None
    return None
