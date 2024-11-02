cars = ['bwm','audi','toyota','subaru']
cars.sort()                                   #永久改变列表排序
print(cars)

print(sorted(cars,reverse=True))             #sorted()函数也可以添加reverse=True参数
cars.reverse()
print(cars)

print(len(cars))