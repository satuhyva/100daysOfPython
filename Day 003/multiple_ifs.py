height = int(input("What is your height in cm? "))

# NOTE: INDENTATION IS ALL-IMPORTANT!!!
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    photo = input("Do you want a photo? (Y or N) ")
    ticket = 0
    if photo == "Y" or photo == "y":
        ticket = 3
    if age < 12:
        ticket += 5
    elif age <= 18:
        ticket += 7
    else:
        ticket += 12
    print(f"Please pay ${ticket}.")
else:
    print("Sorry! No ride for you.")