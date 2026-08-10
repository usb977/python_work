from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()+ die_3.roll()
    results.append(result)
frequencies = []
max_results = die_1.num_sides + die_2.num_sides+ die_3.num_sides
poss_results = range(3, max_results + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "50000次掷3个D6的结果分布图"
labels = {'x':'结果','y':'频率'}  #一个字典
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
#将图形保存到本体文件
# fig.write_html('dice_vidual_d6d10.html')