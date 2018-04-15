# -*- coding:utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter


# 执行API调用并存储响应
proxies={
    "http":"http://127.0.0.1:8580",
    # "https":"http://x.x.x.x:xx"
    }  # https://www.zhihu.com/question/23825711

url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
r = requests.get(url, proxies=proxies)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()  # list类型
submission_dicts = []
for submission_id in submission_ids[:30]:  # 前30帖
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json?print=pretty')
    submission_r = requests.get(url, proxies=proxies)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        # 'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        # 'comments': response_dict.get('descendants', 0)  # 可能评论数为0;dict.get()在指定的键存在时返回对应值,并在指定的键不存在时返回我指定的值（这里是0）
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'value': response_dict.get('descendants', 0)  # 果然得是value才能显示数值
        }
    submission_dicts.append(submission_dict)

topics = []

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)
for submission_dict in submission_dicts:
    # print("\nTitle:  %s" % submission_dict['title'])
    # print("Discussion link:", submission_dict['link'])
    # print("Comments:", submission_dict['comments'])
    topics.append(submission_dict['title'])

# Begin To Draw Histogram
my_style = LS('#beee53', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = '30 New, Top and Best Stories on Hacker News'
chart.x_labels = topics

chart.add('Comments', submission_dicts)  # 就是左边的小方块后的字,为空即不显示
chart.render_to_file('diagram/hn_topics.svg')
