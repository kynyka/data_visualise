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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # if repo_dict['description'].encode('utf-8').find('—'):  # 默认ascii编码,不encode一下,会找不到—
    #     repo_dict['description'] = repo_dict['description'].encode('utf-8').replace('—', '--')

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or '',  #或者写成三元表达式https://segmentfault.com/q/1010000012917291
        'fork':  repo_dict['forks_count'],  # 自定义的key没能显示出来
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()  # 定制图的外观
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14  # 副标签字大小
my_config.major_label_font_size = 18  # 主标签字大小
my_config.truncate_label = 15  # 将较长项目名缩短为15个字符(鼠标移上去会完整显示)
my_config.show_y_guides = False  # y轴参考虚线
my_config.width = 1000  # 图表宽度

chart = pygal.Bar(my_config, style=my_style)  # legend即左侧小方块
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)  # 就是左边的小方块后的字,为空即不显示
chart.render_to_file('diagram/python_repos.svg')
