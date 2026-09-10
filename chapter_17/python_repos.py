"""
@File       : python_repos.py
@Desc       : 通过API查询github上Python语言编写的、Stars超过1万的项目信息
@Author     : Dylan
@LastUpdate : 2026/09/09
@Version    : 1.0

Usage example:
    无示例
"""

import requests

def get_url_state(url):
    """验证服务器是否可联通"""
    headers = {"Accept":"application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    if r.status_code==200:
        return True
    else:
        return False

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

#探索有关仓库的信息
repo_dicts = response_dict['items']    #'items'的值是一个字典列表，每个元素（字典）包含了一个仓库的完整信息
print(f"返回信息的仓库数量：{len(repo_dicts)} ")


print("\n下面是返回的所有仓库信息：")
for repo_dict in repo_dicts:
    print(f"\nName:\t\t{repo_dict['name']}")
    print(f"Owner:\t\t{repo_dict['owner']['login']}")
    print(f"Stars:\t\t{repo_dict['stargazers_count']}")
    print(f"Repository:\t{repo_dict['html_url']}")
    print(f"Created:\t{repo_dict['created_at']}")
    print(f"Updated:\t{repo_dict['updated_at']}")
    print(f"Descirption:\t{repo_dict['description']}")
