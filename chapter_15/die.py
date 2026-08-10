from random import randint

class Die:
    """创建一个骰子的类"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides  #默认是6面，可以传参数

    def roll(self):
        return randint(1,self.num_sides)

