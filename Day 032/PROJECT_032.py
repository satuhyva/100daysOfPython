import smtplib

my_email = "koodimummo@gmail.com"
my_password= ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()   # secure the connection
connection.login(user=my_email, password=)





