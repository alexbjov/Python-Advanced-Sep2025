def forecast(*location_weather):
    sorted_locations = sorted(location_weather, key=lambda x: x[1])
    sunny: list[str] = []
    cloudy: list[str] = []
    rainy: list[str] = []

    for location, weather in sorted_locations:
        if weather == "Sunny":
            sunny.append(f'{location} - {weather}')
        elif weather == "Cloudy":
            cloudy.append(f'{location} - {weather}')
        elif weather == "Rainy":
            rainy.append(f'{location} - {weather}')

    result: list[str] = []
    if sunny:
        sorted_sunny = sorted(sunny)
        result.extend([x for x in sorted_sunny])

    if cloudy:
        sorted_cloudy = sorted(cloudy)
        result.extend([x for x in sorted_cloudy])

    if rainy:
        sorted_rainy = sorted(rainy)
        result.extend([x for x in sorted_rainy])

    return '\n'.join(result)

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
