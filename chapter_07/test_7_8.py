sandwich_orders = ['sdk','kdjf','dsfi']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'已完成：{sandwich} 汉堡！ ')