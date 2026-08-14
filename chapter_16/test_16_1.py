from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_full.csv')  
lines = path.read_text().splitlines()  #按行分割为列表

reader = csv.reader(lines)  #创建一个reader对象
header_row = next(reader)  #next函数返回reader对象的下一行

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

#提取日期和降水量
dates, drops = [], []
for row in reader:      #遍历reader对象余下的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        drop = float(row[5].strip())
    except ValueError:
        print(row[5])
        print(f"{current_date}这天的数据存在缺失！")
    else:
        dates.append(current_date)
        drops.append(drop)

#绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, drops, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = "Daily Drops, 2021\nSitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Drops', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()