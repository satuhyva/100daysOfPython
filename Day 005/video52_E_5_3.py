#Write your code below this row 👇

total = 0

for digit in range(1, 101):
  if (digit % 2 == 0):
    total += digit

print(total)