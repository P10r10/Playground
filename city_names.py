def city_names(city, country):
    return f"{city.title()}, {country.title()}"


def make_album(album, artist, nb_songs=None):
    if nb_songs:
        return {album: artist, "songs": nb_songs}
    return {album: artist}



print(city_names("lisbon", "portugal"))
print(city_names("madrid", "spain"))
print(city_names("paris", "france"))

print(make_album("Thriller", "Michael Jackson"))
print(make_album("Abbey Road", "The Beatles"))
print(make_album("The Dark Side of the Moon", "Pink Floyd"))
print(make_album("Rumours", "Fleetwood Mac", 11))
print(make_album("21", "Adele", 11))

while True:
    artist = input("Artist name? (q to quit): ")
    if artist == "q":
        break
    album = input("Album name? (q to quit): ")
    if album == "q":
        break
    print(make_album(album, artist))

