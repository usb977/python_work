'''
初步认识什么是字典
列表用[]  字典用{}
'''

alien_0 = {'color':'green','points':5}   #“键值对”，用冒号分割   冒号后可以关联任意对象

# print(alien_0['color'])     #通过键访问值的时候需要用方括号来索引
# print(alien_0['points'])

new_points = alien_0['points']
print(f'你刚刚消灭了一个{alien_0["color"]}颜色的外星人，获得了{new_points}点分数！')