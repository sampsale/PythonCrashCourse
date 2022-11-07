sandwich_orders = ["tuna", "cheese", "tomato", "cucumber"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()    
    print(f"\tI made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print("\n")
for finished in finished_sandwiches:
    print(f"\tFinished sandwich: {finished}")


