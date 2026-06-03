from random import randint,choice

print(randint(1,10))

players = ['charles','martina','florence','eli']
first_up = choice(players)    #该函数入参可以是列表或者元组
print(first_up)