print("\n\nWELCOME TO THE TIP CALCULATOR!\n")
total = float(input("What was the total bill (€)?\n"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = float(input("How many people to split the bill?\n"))
toPay = ((1 + percentage / 100) * total ) / people
print(f"Each person should pay: {toPay:.2f}€.")
