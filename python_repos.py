# -*- coding:utf-8 -*-
import requests


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # 存储api调用的url
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()  # 方法json()将API返回的json格式的信息转换为一个Python字典
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

print('\nSelected information about first repository:')
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
