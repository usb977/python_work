from random import randint

class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides = randint(1,6)  #包括6
        print(self.sides)

die1 = Die()

# while(i<=10):
#     print(f"第{i}次投掷结果为：")
#     die1.roll_die()
#     i+=1

for i in range(1,11):
    print(f"第{i}次投掷结果为：")
    die1.roll_die()