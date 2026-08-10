import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x_label = range(1,5001)
y_label = [x**3 for x in x_label]

ax.scatter(x_label, y_label, c=y_label, cmap=plt.cm.Blues, s=10)

plt.show()