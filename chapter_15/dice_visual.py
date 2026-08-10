from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "1000次掷2个骰子的结果分布图"
labels = {'x':'结果','y':'频率'}  #一个字典
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()