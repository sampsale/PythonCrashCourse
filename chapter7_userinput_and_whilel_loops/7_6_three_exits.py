

toppings = []

prompt = '\tPlease enter a topping. When you are done, type "quit": '

active = True

topping = input(prompt)
while True:
    toppings.append(topping)
    print(f"\tAdding {topping}")
    topping = input(prompt)
    if topping == 'quit':
        break

print("\tAdded toppings:")
for top in toppings:
    print(f"\t\t{top}") 