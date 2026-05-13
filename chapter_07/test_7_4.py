prompt = '\nPlease enter the toppings of pizza you want to add:'
prompt += '\nEnter quit to end the program.'

flag = True

while flag:
    topping = input(prompt)
    if topping == 'quit':
        flag=False
    else:
        print(f"\nOK, I have put the {topping} into the pizza! "
              "Anything else?")