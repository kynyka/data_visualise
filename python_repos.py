# -*- coding:utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 存储api调用的url
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()  # 方法json()将API返回的json格式的信息转换为一个Python字典
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))  # https://api.github.com/rate_limit这里看API的速率限制

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)

my_cofig = pygal.Config()  # 定制图的外观
my_cofig.x_label_rotation = 45
my_cofig.show_legend = False
my_cofig.title_font_size = 24
my_cofig.label_font_size = 14  # 副标签字大小
my_cofig.major_label_font_size = 18  # 主标签字大小
my_cofig.truncate_label = 15  # 将较长项目名缩短为15个字符(鼠标移上去会完整显示)
my_cofig.show_y_guides = False
my_cofig.width = 1000

chart = pygal.Bar(my_config, style=my_style)  # legend即左侧小方块
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)  # 就是左边的小方块后的字,为空即不显示
chart.render_to_file('diagram/python_repos.svg')
