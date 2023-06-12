toppings = []
while True:
    topping = input("Pizza topping? (quit to exit): ")
    if topping == "quit":
        break
    toppings.append(topping)
    print(topping, "added!")