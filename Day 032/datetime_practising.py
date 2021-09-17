import datetime as dt

current_datetime = dt.datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.weekday())   #MON = 0

date_of_something = dt.datetime(year=2000, month=3, day=12)
print(date_of_something)
date_of_something_else = dt.datetime(year=2000, month=3, day=12, hour=14, minute=33, second=23)
print(date_of_something_else)

import smtplib
import secrets
import random

MY_EMAIL = "koodimummo@gmail.com"
RECIPIENT_EMAIL = "koodimummo@yahoo.com"
PASSWORD = secrets.password

today = dt.datetime.now()
if today.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(MY_EMAIL, PASSWORD)
        with open("quotes.txt") as file:
            lines = file.readlines()
            randomNumber = random.randint(0, len(lines) - 1)
            print(lines[randomNumber])

        server.sendmail(
            MY_EMAIL,
            RECIPIENT_EMAIL,
            f"Subject:MOTIVATION\n\n{lines[randomNumber]}"
        )
