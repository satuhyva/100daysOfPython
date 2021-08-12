#Write your code below this row 👇

for digit in range(1, 101):
  toPrint = ""
  if digit % 3 == 0:
    toPrint += "Fizz"
  if digit % 5 == 0:
    toPrint += "Buzz"
  if toPrint == "":
    toPrint = digit
  print(toPrint)