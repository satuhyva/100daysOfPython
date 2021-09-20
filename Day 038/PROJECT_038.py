from secrets import nutritionix_id, nutritionix_api_key, sheety_workouts_api, sheety_token
import requests
from datetime import datetime

# Get exercise data and calories
user_input = input("Tell me what exercise you did? ")
request_body = {
    "query": user_input,
    "gender": "female",
    "weight_kg": "60",
    "height_cm": "175",
    "age": "45"
}
headers = {
    "x-app-id": nutritionix_id,
    "x-app-key": nutritionix_api_key
}

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response_nutritionix = requests.post(exercise_url, json=request_body, headers=headers)
response_nutritionix.raise_for_status()



# Save data to google sheet with help of sheety
sheety_url = sheety_workouts_api
for activity in response_nutritionix.json()["exercises"]:
    # Python datetime formatting:
    # https://www.w3schools.com/python/python_datetime.asp
    timeNow = datetime.now()
    # date etc. need to be lowercase!!!,  workout is needed
    request_body_sheety = {
        "workout": {
            "date": timeNow.strftime("%x"),
            "time": timeNow.strftime("%X"),
            "exercise": activity["user_input"],
            "duration": str(int(activity["duration_min"])),
            "calories": str(int(activity["nf_calories"])),
        }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {sheety_token}"
    }

    response_sheety = requests.post(url=sheety_url, json=request_body_sheety, headers=headers)
    response_sheety.raise_for_status()






