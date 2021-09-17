from datetime import datetime
import random
import smtplib
import secrets


MY_EMAIL = "koodimummo@gmail.com"
RECIPIENT_EMAIL = "koodimummo@yahoo.com"
PASSWORD = secrets.password

today = datetime.now()

with open("birthdays.csv") as file:
    data = file.readlines()
    birthdays = []
    for line in data:
        components = line.split(",")
        if components[-1].strip() != "day":
            if int(components[-1].strip().replace("\n", "")) == today.day and int(components[-2].strip().replace("\n", "")) == today.month:
                birthdays.append({
                    "name": components[0],
                    "email": components[1],
                })

if len(birthdays) > 0:
    files = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
    letter_base_file_name = random.choice(files)
    all_messages = []

    with open(letter_base_file_name, mode="r") as letter_base_file:
        letter_base_lines = letter_base_file.readlines()
        for person in birthdays:
            message_lines = []
            for line in letter_base_lines:
                message_lines.append(line.replace("[NAME]", person["name"]).replace("\n", ""))
            message = '\n'.join(message_lines)
            all_messages.append({ "name": person["name"], "message": message})

    print(all_messages)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(MY_EMAIL, PASSWORD)
        for mail in all_messages:
            server.sendmail(
                MY_EMAIL,
                RECIPIENT_EMAIL,
                f"Subject:HAPPY BIRTHDAY {mail['name']}\n\n{mail['message']}"
            )

# https://www.pythonanywhere.com
