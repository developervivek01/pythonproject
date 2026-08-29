"""DAY 35 OF 100 DAYS OF 
PYTHON PROJECT"""

import requests

city = input("Enter city name: ")

geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city}
).json()

lat = geo["results"][0]["latitude"]
lon = geo["results"][0]["longitude"]
name = geo["results"][0]["name"]

data = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": lat, "longitude": lon, "current_weather": True}
).json()

temp = data["current_weather"]["temperature"]
wind = data["current_weather"]["windspeed"]

print(f"\nCity: {name}")
print(f"Temp: {temp} °C")
print(f"Wind speed: {wind} km/h")