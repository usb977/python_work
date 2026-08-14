from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_weather_data(filename):
    """读取天气CSV，返回(日期, 最高温, 最低温)三个列表"""
    path = Path(filename)
    lines = path.read_text().splitlines() #分割为列表
    reader = csv.DictReader(lines)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        try:
            high = int(row['TMAX'])
            low = int(row['TMIN'])
        except ValueError:
            print(f"{current_date}这一天存在数据缺失！")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

dates_sk, highs_sk, lows_sk = read_weather_data('weather_data/sitka_weather_2021_simple.csv')
dates_dv, highs_dv, lows_dv = read_weather_data('weather_data/death_valley_2021_simple.csv')

# 绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

for dates, highs, lows, color, label in [
    (dates_sk, highs_sk, lows_sk, 'red', 'Sitka'),
    (dates_dv, highs_dv, lows_dv, 'blue', 'Death Valley'),   #元组列表
]:
    ax.plot(dates, highs, color=color, alpha=0.5, label=f"{label} high")
    ax.plot(dates, lows, color=color, alpha=0.5, label=f"{label} low")
    ax.fill_between(dates, highs, lows, facecolor=color, alpha=0.1)

ax.set_title("Daily High and Low Temperatures, 2021", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.ylim(10, 140)
plt.legend()
plt.show()