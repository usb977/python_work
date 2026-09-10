"""
@File       : hn_article.py
@Desc       : 通过API获取Hacker News上某篇文章的信息
@Author     : Dylan
@LastUpdate : 2026/09/09
@Version    : 1.0

Usage example:
    无示例
"""

import requests
import json

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#探索数据的结构
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4) #使用indent参数指定嵌套元素的缩进量为4
print(response_string)



