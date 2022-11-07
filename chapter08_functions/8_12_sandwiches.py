

def make_sandwich(*toppings):
    print("\n\tMaking sandwich with following ingredients:")
    for topping in toppings:
        print(f"\t\t{topping}")


make_sandwich('tuna', 'cheese', 'butter')
make_sandwich('tuna', 'cheese')
make_sandwich('tuna', 'shrimp', 'tomato', 'salad')
