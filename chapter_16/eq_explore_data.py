"""
@File       : eq_explore_data.py
@Desc       : 从geojson文件中提取地震数据
@Author     : Dylan
@LastUpdate : 2026/08/26
@Version    : 1.0

Usage example:
    无示例
"""

from pathlib import Path
import json

#把文件当字符串读入，然后转为对应的Python对象（这里转成了dict）
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()           #content是python字符串
all_eq_data = json.loads(contents)  

# #将数据文件转换为更易于阅读的geojson文件
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4) #指定嵌套元素的缩进量为4
# path.write_text(readable_contents)

#查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']  #这个是一个列表，记录了160次地震具体信息
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])