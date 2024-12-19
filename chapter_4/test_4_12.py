my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]        #复制列表内容到新列表
  
my_foods.append('cannolli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)