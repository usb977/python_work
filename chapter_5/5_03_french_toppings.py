available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese')   #圆括号表示元组，即不可修改的列表

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
        
print("\nFinished making your pizza!")