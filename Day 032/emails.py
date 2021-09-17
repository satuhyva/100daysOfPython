# smtp = simple mail transport protocol
import smtplib
import secrets

# https://stackoverflow.com/questions/57598232/timed-out-error-when-using-python-to-send-an-email
# kurssin ohje ei toimi...

MY_EMAIL = "koodimummo@gmail.com"
RECIPIENT_EMAIL = "koodimummo@yahoo.com"
PASSWORD = secrets.password


with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(MY_EMAIL, PASSWORD)
    server.sendmail(
        MY_EMAIL,
        RECIPIENT_EMAIL,
        "Subject=AIHE\n\nBODY......eeee....."
    )

# kun with ..., ei tarvita server.quit()

