prompt = '\nPlease enter a city you have visited: '
prompt += '\nEnter "quit" when you finished.'

while True:
    city = input(prompt)

    if city == 'quit':
        break    #退出while循环
    else:
        print(f"I'd love to go to {city.title()}!")