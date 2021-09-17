import requests
from datetime import datetime
import smtplib
import secrets
import time


MY_LAT = 60.192059
MY_LONG = 24.945831
MY_EMAIL = "koodimummo@gmail.com"
RECIPIENT_EMAIL = "koodimummo@yahoo.com"
PASSWORD = secrets.password


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sun_data = response.json()
sunrise_hours = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hours = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
time_now_hours = datetime.now().hour


def get_is_close_enough():
    is_close_enough = False
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        print("Close enough!")
        is_close_enough = True
    else:
        print("Too far!")
    return is_close_enough


def get_is_dark_enough():
    is_dark_enough = False
    if sunrise_hours < time_now_hours < sunset_hours:
        print("Not dark enough!")
    else:
        print("It is dark enough!")
        is_dark_enough = True
    return is_dark_enough


while True:
    time.sleep(60 * 30) # every 30 minutes
    if get_is_close_enough() and get_is_dark_enough:
        hours_remaining_till_sunrise = 0
        if time_now_hours < sunrise_hours:
            hours_remaining_till_sunrise = sunrise_hours - time_now_hours
        else:
            hours_remaining_till_sunrise = sunrise_hours + 24 - time_now_hours
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(MY_EMAIL, PASSWORD)
            server.sendmail(
                MY_EMAIL,
                RECIPIENT_EMAIL,
                f"Subject:ISS \nGo see the ISS, you have {hours_remaining_till_sunrise} hours left till sunrise!"
            )
        print("Mail sent!")


