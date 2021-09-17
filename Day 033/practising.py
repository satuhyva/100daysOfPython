# 1XX: hold on
# 2XX: kaikki ok
# 3XX: mene pois, redirection
# 4XX: you screwed up
# 5XX: API-päässä ongelma

# https://www.latlong.net
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# https://sunrise-sunset.org/api


import requests
from datetime import datetime

iss_url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=iss_url)
response.raise_for_status()  # modulin valmis toiminto, joka hoitelee kaikki mahdolliset virheet

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
position = (latitude, longitude)
print(position)

# HELSINKI:
# Longitude: 24.945831
# Latitude: 60.192059

MY_LOCATION = {"lat": 60.192059, "lng": 24.945831}
SUN_URL = "https://api.sunrise-sunset.org/json"

# sun_response = requests.get(url=SUN_URL, params=MY_LOCATION)
sun_response = requests.get(f"{SUN_URL}?lat={MY_LOCATION['lat']}&lng={MY_LOCATION['lng']}&formatted=0")
sun_response.raise_for_status()

sun_data = sun_response.json()
sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]

sunrise_hours = int(sunrise.split("T")[1].split(":")[0])
sunset_hours = int(sunset.split("T")[1].split(":")[0])
current_hours = datetime.now().hour
print(sunrise_hours)
print(sunset_hours)
print(f" {sunrise_hours}, {current_hours}, {current_hours}")
