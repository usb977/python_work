from random import choice

class RandomWalk:
    """一个生成随机游走的类"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        #初始值从0开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走包含的所有点"""
        while len(self.x_values)<self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step==0 and y_step==0:
                continue    #跳过当前循环进入下一轮

            x = self.x_values[-1] + x_step   #下标-1表示列表最后一个元素
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step