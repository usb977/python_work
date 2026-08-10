from die import Die
from collections import Counter
import plotly.express as px


die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll()+die_2.roll() for _ in range(50000)]

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)

frequencies = [Counter(results)[value] for value in poss_results]

title = "50000次掷2个D8点数相加的结果分布图"
labels = {'x':'结果','y':'频率'}  #一个字典
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
#将图形保存到本体文件
# fig.write_html('dice_vidual_d6d10.html')