holiday_places = {}
flag = True

while flag:
    name = input('\n请输入您的名字：')
    place = input('\n如果有机会，您想去什么地方度假：')
    holiday_places[name] = place
    
    go_on = input('\n是否继续调查？请输入yes/no：')
    if go_on=='no':
        flag = False
    elif go_on == 'yes':
        flag = True
    else:
        print('\n请检查您输入的格式！')
        break

for k,v in holiday_places.items():
    print(f"{k} want to go {v} for holiday!")