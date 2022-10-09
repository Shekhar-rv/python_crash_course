def city_country(city: str, country: str, population: int = "") -> str:
    """Takes the city and country name and returns a neatly formatted string"""
    if population:
        location_name = ", ".join([city, country])
        location_data = location_name + f" - population {population}"
    else:
        location_data = ", ".join([city, country])
    formatted_location_name = location_data.title()
    print("formatted_location_name: ", formatted_location_name)
    return formatted_location_name


if __name__ == "__main__":
    test1 = city_country("santiago", "chile", 325000)
