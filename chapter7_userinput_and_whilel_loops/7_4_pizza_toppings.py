

toppings = []

prompt = '\tPlease enter a topping. When you are done, type "quit": '

topping = input(prompt)
while topping != 'quit':
    toppings.append(topping)
    print(f"\tAdding {topping}")
    topping = input(prompt)
    

print("\tAdded toppings:")
for top in toppings:
    print(f"\t\t{top}") 