# -*- coding:utf-8 -*-
import pygal.maps.world as pmw


wm = pmw.World()
wm.title = 'Populations of Countries in North America'

wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})  # 第二个实参也接受字典;颜色最淡人数最少

wm.render_to_file('diagram/na_populations.svg')
