from random import choices  #有放回的抽样
from random import sample

numbers = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']

lucky_num = sample(numbers,4)
# lucky_num2 = choices(numbers,k=4)
print(f"中奖的数字是：{lucky_num}")

i=0
while True:
    i+=1
    my_ticket = sample(numbers,4)
    if(my_ticket==lucky_num):
        print(f"恭喜!您抽中大奖了，一共尝试了 {i} 次！")
        break