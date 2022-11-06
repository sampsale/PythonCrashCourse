sandwich_orders = ["pastrami", "tuna", "cheese",
                   "pastrami", "tomato", "cucumber", "pastrami"]

finished_sandwiches = []

print("\tWe are out of Pastrami sandwiches! \n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:

    sandwich = sandwich_orders.pop()
    print(f"\tI made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print("\n")
for finished in finished_sandwiches:
    print(f"\tFinished sandwich: {finished}")
