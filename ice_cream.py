from restaurants import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours: list[str]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        print("Our flavours:\n", ", ".join(self.flavours))


ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream",
]

my_stand = IceCreamStand("I Scream", "deserts", ice_cream_flavors)
my_stand.display_flavours()
my_stand.describe_restaurant()
