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

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))  # 仔细查看这些键,可大致知道可提取有关项目的哪些信息(要准确地获悉API将返回哪些信息,要么阅读文档,要么像此处这样使用代码来查看这些信息【实际浏览器里打上地址看时就能了解信息了】)
# for key in sorted(repo_dict.keys()):
#     print(key)

print('\nSelected information about first repository:')
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
