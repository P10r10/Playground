def city_country(city: str, country: str, population: int = None) -> str:
    if population:
        return f"{city.capitalize()}, {country.capitalize()}" \
            f" - population {population}"
    else:
        return f"{city.capitalize()}, {country.capitalize()}"
