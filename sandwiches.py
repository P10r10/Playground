def sandwiches(*ingredients):
    print("The ingredients are:")
    for ingredient in ingredients:
        print(f"\t-{ingredient}")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


sandwiches("lettuce", "tomato", "cheese", "ham")
sandwiches("cheese", "ham")
sandwiches("olives")

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
user_profile = build_profile('almeida', 'santiago',
                             hobbies=["running", "chess"],
                             status="married")
print(user_profile)


sandwich_ingredients = [
    "lettuce",
    "tomato",
    "cheese",
    "ham",
    "turkey",
    "bacon",
    "mayonnaise",
    "mustard",
    "pickles",
    "onions",
    "avocado",
    "cucumber",
    "bell peppers",
    "olives",
    "salt",
    "pepper",
]
