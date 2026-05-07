pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],  #用列表作为字典的值
}

print(f'You ordered a {pizza["crust"]}-crust pizza' 
      'with the following topping:')

for topping in pizza['toppings']:
    print(f'\t{topping}')