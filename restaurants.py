class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}. We serve {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self):
        print(f"Hi, {self.first_name} {self.last_name}!")


if __name__ == "__main__":
    my_restaurant = Restaurant("Natraj", "Indian")
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    person = User("Almeida", "Santiago", 49)
    person.greet()
    print(f"You don't look like {person.age}.")
