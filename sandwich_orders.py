sandwich_orders = [
    "Turkey Club",
    "BLT",
    "Chicken Parmesan",
    "Veggie Wrap",
    "Steak and Cheese",
]
finished_sandwiches = []

while sandwich_orders:
    done =sandwich_orders.pop()
    print(f"I made your {done} sandwich.")
    finished_sandwiches.append(done)

print("Finished: ", finished_sandwiches)
