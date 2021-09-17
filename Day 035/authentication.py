# API authentication

# https://openweathermap.org/price
import requests
from secrets import open_weather_api_key

open_weather_endpoint = "http://api.openweathermap.org/data/2.5/weather"
CITY = "helsinki"
url = f"{open_weather_endpoint}?q={CITY}&appid={open_weather_api_key}"

response = requests.get(url=url)
weather = response.json()
print(weather)

# OR with params:
my_params = {
    "q": CITY,
    "appid": open_weather_api_key
}
response2 = requests.get(url, params=my_params)
weather2 = response2.json()
print(weather2)


# json-viewer
# http://jsonviewer.stack.hu

example_weather = {"coord": {"lon": 24.9355, "lat": 60.1695},
            "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}],
            "base": "stations",
            "main": {"temp": 277.97, "feels_like": 274.72, "temp_min": 275.92, "temp_max": 279.69, "pressure": 1015, "humidity": 86},
            "visibility": 10000,
            "wind": {"speed": 4.12, "deg": 300},
            "clouds": {"all": 75},
            "dt": 1631681768,
            "sys": {"type": 2, "id": 2019088, "country": "FI", "sunrise": 1631677683, "sunset": 1631724188},
            "timezone": 10800,
            "id": 658225,
            "name": "Helsinki",
            "cod": 200
            }
