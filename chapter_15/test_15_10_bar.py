from die import Die
import matplotlib.pyplot as plt

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "1000 D6 dice result"

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies, width=1, edgecolor="white", linewidth=0.7)
ax.set_title(title)
plt.show()