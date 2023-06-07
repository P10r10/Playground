person_1 = {
    "first_name": "alexandre",
    "last_name": "almeida",
    "city": "porto",
    "age": 49,
    "fav_numbers": [15, 31, 66],
}
person_2 = {
    "first_name": "fátima",
    "last_name": "ferreira",
    "city": "viseu",
    "age": 53,
    "fav_numbers": [14],
}
person_3 = {
    "first_name": "rui",
    "last_name": "simões",
    "city": "braga",
    "age": 28,
    "fav_numbers": [0, 100],
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"With an age of {person['age']}, this is {full_name} from "
          f"{person['city'].title()}. The favourite numbers are: ", end="")
    for number in person["fav_numbers"]:
        print(f"{number} ", end="")
    print()

brand = input("What kind of car? ")
print(f"Let me see if I can find you a {brand.title()}.")
people = int(input("How many people for dinner? "))
if people > 8:
    print("You have to wait for a table.")
else:
    print("Your table is ready!")
number = int(input("Pick a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
