# -*- coding:utf-8 -*-
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['public-apis', 'httpie', 'flask', 'django']
plot_dicts = [
    {'value': 35548, 'label': 'Description of public-apis.'},
    {'value': 34898, 'label': 'Description of httpie.'},
    {'value': 34715, 'label': 'Description of flask.'},
    {'value': 33198, 'label': 'Description of django.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('diagram/bar_descriptions.svg')