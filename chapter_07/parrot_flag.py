#该程序需要从终端运行
prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter "quit" to end the program.'

active = True
while active == True:
    message = input(prompt)
    
    if message != 'quit':   #避免打印quit
        print(message)
    else:
        active = False