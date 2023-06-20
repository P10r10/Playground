class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}. We serve {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, nb: int):
        self.number_served = nb

    def increment_number_served(self, nb: int):
        self.number_served += nb


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def greet(self):
        print(f"Hi, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == "__main__":
    my_restaurant = Restaurant("Natraj", "Indian")
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    person = User("Almeida", "Santiago", 49)
    person.greet()
    print(f"You don't look like {person.age}.")
    print(my_restaurant.number_served)
    my_restaurant.number_served = 15
    print(my_restaurant.number_served)
    my_restaurant.set_number_served(89)
    print(my_restaurant.number_served)
    my_restaurant.increment_number_served(11)
    print(my_restaurant.number_served)
    print(person.login_attempts)
    for _ in range(1000):
        person.increment_login_attempts()
    print(person.login_attempts)
    person.reset_login_attempts()
    print(person.login_attempts)
