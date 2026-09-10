"""
@File       : python_repos_visual.py
@Desc       : 将API查询到的github上的项目信息，使用Plotly制作可交互的图
@Author     : Dylan
@LastUpdate : 2026/09/09
@Version    : 1.0

Usage example:
    无示例
"""

import requests
import plotly.express as px

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"   #太长了所以分行写

headers = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")

#将响应的json格式文本转为字典
response_dict = r.json()
print(f"符合要求的仓库数量：{response_dict['total_count']}")
print(f"查询结果是否完整：{not response_dict['incomplete_results']}")

#处理有关仓库的信息
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    #将仓库名转化为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"  #定制柱状图的悬停显示文本
    hover_texts.append(hover_text)

#可视化
title = "GitHub上最受欢迎的项目"
labels = {'x':'仓库名称','y':'加星数'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts) #横坐标是仓库名称，纵坐标是star数量
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)   #0是完全透明，1是完全不透明
fig.show()
