fruits = ["apple", "peach", "cherry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


for number in range(1,3):       ## 1, 2  (1 in included, 3 is not)
    print(number)

for digit in range(0, 5):       # 0,1,2,3,4
    print(digit)

print("***************")
for index in range(1, 10, 3):       # 1, 4, 7  (last number defines the step, the upper limit is not included)
    print(index)

# Count the sum of 1 + 2 + 3 + ... + 99 + 100:
total = 0
for number in range(1, 101):
    total += number
print(total)