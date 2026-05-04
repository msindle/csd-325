
def city_country(city, country, population=None, language=None):
    """Return a formatted city-country string with optional population and language."""
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language.title()}"

    return result


# Required calls for the assignment
print(city_country("santiago", "chile"))
print(city_country("santiago", "chile", 5000000))
print(city_country("santiago", "chile", 5000000, "spanish"))