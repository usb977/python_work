prompt1 = "\n任何时候按下q即可退出程序！"
prompt1 += "\n请输入第一个数："
prompt2 = "\n任何时候按下q即可退出程序！"
prompt2 += "\n请输入第二个数："

flag = True

while flag:
    num1 = input(prompt1)
    if num1 == 'q':
        flag = False
        break
    num2 = input(prompt2)
    if num2 == 'q':
        flag = False
        break
    
    try:
        num_sum = int(num1) + int(num2)
    except ValueError:
        print("\n**********请检查您的输入格式！**********")
    else:
        print(f"\n**********您输入的两个数的和为： {num_sum} ! **********")