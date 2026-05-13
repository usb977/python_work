#在终端运行
responses = {}
flag = True

while flag:
    name = input("\n请输入您的名字：")
    response = input("\n如果有机会，您会去爬哪座山：")
    responses[name] = response

    repeat = input('\n你还想让其他人回答吗（yes/no）：')
    if repeat == 'no':
        flag = False

print('\n---调查结果---')
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")