"""
@File       : eq_world_map.py
@Desc       : 从geojson文件中提取地震数据，并用plotly绘制全球地震散点图
@Author     : Dylan
@LastUpdate : 2026/08/26
@Version    : 1.0

Usage example:
    无示例
"""

import plotly.express as px
from pathlib import Path
import json
import pandas as pd

#把文件当字符串读入，然后转为对应的Python对象（这里转成了dict）
path = Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()           #content是python字符串
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)  

#查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']  #这个是一个列表，记录了160次地震具体信息
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags),
    columns=['经度', '纬度', '位置', '震级']
)     #将需要的数据封装为一个字典 
print(data.head())   #在终端打印前5行数据

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=all_eq_data['metadata']['title'], #提取原数据中的标题作为图的标题
    size='震级',
    size_max=10,
    color_continuous_scale='greens',
    color='震级', #默认渐变色从小到大对于：蓝—>红—>黄
    hover_name='位置',
)

fig.show()

