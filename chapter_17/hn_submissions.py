"""
@File       : hn_submissions.py
@Desc       : 通过API获取Hacker News主页排名靠前文章的信息
@Author     : Dylan
@LastUpdate : 2026/09/09
@Version    : 1.0

Usage example:
    无示例
"""

from operator import itemgetter
import requests

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)  #get到的是一个文章ID列表
print(f"Status code: {r.status_code}")

#处理有关每篇文章的信息
submission_ids = r.json()  #转化为Python列表，有500个元素
submission_dicts = []
for submission_id in submission_ids[:5]:   #获取列表切片：前5个文章的id
    #对于每篇文章，都执行一个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # print(response_dict)

    #提取每篇文章的信息，拼凑一个新字典
    submission_dict = {
        'title':response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)  #按照评论数量排序

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"Discussion link:{submission_dict['hn_link']}")
    print(f"Comments:{submission_dict['comments']}")




