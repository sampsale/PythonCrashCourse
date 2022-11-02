my_pizzas = ['frutti di mare', 'salami', 'kebab-smetana']
friend_pizzas = my_pizzas[:]

my_pizzas.append('pepperoni')
friend_pizzas.append('vegetarian')

print(my_pizzas)
print(friend_pizzas)

print('My favorite pizzas are: ')
for pizza in my_pizzas:
    print(f'\t{pizza.title()}')

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(f'\t{pizza.title()}')