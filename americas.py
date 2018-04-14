# -*- coding:utf-8 -*-
import pygal.maps.world as pmw


wm = pmw.World()  # 原先的pygal.Worldmap()已无,改至如此
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])  # 标签和列表,列表里是要突出的国家的国别码;每次调用add都会为指定的国家选择一种颜色
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('diagram/americas.svg')
