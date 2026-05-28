def make_pizza(size, *toppings):
    print(f'\n制作一个{size}-英寸的披萨，用以下这些配料：')
    for topping in toppings:
        print(f'- {topping}')