pizzas = ['pizzahut','domino','babela']
friend_pizzas = pizzas[:]
pizzas.append("Hungry Howie's")
friend_pizzas.append("Papa John's")

print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)