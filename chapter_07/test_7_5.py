prompt = '\nPlease enter your age:'
prompt += '\nEnter quit to end the program.'

flag = True

while flag:
    text = input(prompt)
    if text=='quit':
        break
    
    try:
        num = int(text)
        if num<3:
            print('You are free!')
        elif num<12:
            print('You need to pay $10.00!')
        elif num>=12:
            print('You need to pay $15.00!')
    except ValueError:
        print('检查您的输入格式，只接受数字输入!')