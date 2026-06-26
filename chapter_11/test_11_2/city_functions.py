def city_func(city,country,population = None):
    if population:
        name = f"{city.title()}, {country.title()} - population {population}"
    else:
        name = f"{city.title()}, {country.title()}"
    return name