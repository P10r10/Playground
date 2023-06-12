sandwich_orders = [
    "Turkey Club",
    "Pastrami",
    "BLT",
    "Chicken Parmesan",
    "Pastrami",
    "Veggie Wrap",
    "Steak and Cheese",
    "Pastrami",
]
finished_sandwiches = []

print("We've run out of pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    done =sandwich_orders.pop()
    print(f"I made your {done} sandwich.")
    finished_sandwiches.append(done)

print("Finished: ", finished_sandwiches)
