def make_shirt(size=66, message="I love Python"):
    """I'm the t-shirt maker!"""
    print(f'The t-shirt is size {size} and the message is "{message}".')


def describe_city(city, country="Portugal"):
    """Geography master!"""
    print(f"{city} is in {country}.")


make_shirt(44, "Hell yeah!")
make_shirt(message="Ahoy!", size=55)
make_shirt(size=33)
make_shirt(size=77, message="hahaha")
describe_city("Lisbon")
describe_city("Porto")
describe_city("Paris", country="France")
