cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if (car == 'bmw'):       # if后面的条件可以不加括号，这里加括号是为了增加可读性
        print(car.upper())
    else:
        print(car.title())