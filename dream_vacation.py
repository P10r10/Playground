places = []

while True:
    prompt = "If you could visit one place in the world, where would you go? "
    place = input(prompt)
    if place == "":
        break
    places.append(place)
print("Places are: ", places)
