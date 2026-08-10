import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=100)
    point_numbers = range(rw.num_points)
    #将点的边缘设为无轮廓
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors= 'none', s=15)
    ax.set_aspect('equal')    #指定坐标轴刻度相等
    #突出起点和终点
    ax.scatter(0,0,c='green', edgecolors= 'none',s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors= 'none',s=100)
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_walking = input("要再生成一张图吗? (y/n):")
    if keep_walking == 'n':
        break