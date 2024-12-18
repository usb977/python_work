squares = []
for value in range(1,11):
    square = value ** 2          #在python中，**表示乘方运算
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,12)]        #利用列表推导式来生成数值列表
print(squares)