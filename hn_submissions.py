# -*- coding:utf-8 -*-
import requests

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
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
    print("\nTitle:  %s" % submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
