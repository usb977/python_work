sandwich_orders = ['pastrami','sdk','pastrami','kdjf','dsfi','pastrami']
print(sandwich_orders)
print("pastrami已经卖完了")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)