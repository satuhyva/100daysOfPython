import requests
from secrets import open_weather_api_key, twilio_phone_number, twilio_account_sid, twilio_account_token
from twilio.rest import Client

# pip3 install twilio


# "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

open_weather_one_call_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

my_location = (60.192059, 24.945831)

parameters = {
    "lat": my_location[0],
    "lon": my_location[1],
    "exclude": "current,minutely,daily,alerts",
    "appid": open_weather_api_key
}

response = requests.get(open_weather_one_call_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"]
weather_before_12 = weather_data[0:12]  # we only want the first next 12 hours

weather_conditions = []
for hour in weather_before_12:
    weather_id = hour["weather"][0]["id"]
    weather_main = hour["weather"][0]["main"]
    if weather_main not in weather_conditions:
        weather_conditions.append(weather_main)

take_umbrella = False
if 'Rain' in weather_conditions or 'Drizzle' in weather_conditions or 'Thunderstorm' in weather_conditions:
    take_umbrella = True

message_body_text = f"Todays weather (next 12 hours): {','.join(weather_conditions)}."
if take_umbrella:
    message_body_text += " Take an umbrella with you!"
print(message_body_text)

# Costs a lot!
#client = Client(twilio_account_sid, twilio_account_token)
#message = client.messages.create(
    #body=message_body_text,
    #from_=twilio_phone_number,
    #to='+358503810631'
#)
