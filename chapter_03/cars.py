cars = ['bwm','audi','sobaru','toyota']
cars.reverse()            #翻转顺序--永久
print(cars)

cars.sort()               #顺序排序--永久
print(cars)

cars.sort(reverse=True)   #逆序排序--永久
print(cars)

print(sorted(cars))       #顺序排序--临时
print(sorted(cars,reverse=True))

num = len(cars)
print(f'列表的长度为 {num} !')