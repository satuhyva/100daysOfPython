# Day 1: Strings, variables

name = input("What is your name? ")
print("Your name is " + name)
name = "Angela"
print("Now your name is " + name)
length = len(name)
print("Length of your name is " + str(length))



# Day 2: Data types

# String
print("01234"[1])  # "1"
print("22" + "33")  # "2233"

# Integer
print(1_000_000)  # 1000000

# Float
pii = 3.14

# Boolean
t = True
f = False

# What type?
numberOfCharacters = len(input("Your name? "))
print(type(numberOfCharacters))  # <class 'int'>

# Type casting or conversion:
numberOfCakes = 5
numberAsString = str(numberOfCakes)
print("There are " + numberAsString + " cakes.")

# Math operations:
a = 1 + 1
b = 3 - 4
c = 4 * 6
d = 6 / 4  # result is always a float
e = 2 ** 3  # 8 (exponent, power)

# Number manipulation:
numberDecimals = 0.123456789
print(f"Three decimals of {numberDecimals}: {numberDecimals:.3f}")  # Three decimals of 0.123456789: 0.123




# Day 3: If, else
x = 5
y = 5
print(x == y)
print(not True)
if x > 10 and y < -33:
    print("is not")
else:
    print("else")

age = int(input("What is your age? "))
if age < 12:
    print("Please pay $5.")
elif age <= 18:
    print("Please pay $7.")
else:
    print("Please pay $12.")




# Day 4: Random, list
import random

random_number = random.randint(1, 4)  # 1, 2, 3 OR 4
print(random_number)
# Random number between 0.0 and 1.0. (0.0 is included, 1.0 is not! => 0.0 - 0.999999.....)
print(random.random())
# To get random numbers between 0.0 - 5:
print(random.random() * 5)

fruits = ["apple", "orange", "cherry", "pear"]
print(fruits[0])    # apple
print(fruits[-1])   # pear

fruits[-3] = "coconut"          # ["apple", "coconut", "cherry", "pear"]
print(fruits[1])    # coconut

fruits.extend(["banana", "plum"])
print(fruits[4])    # banana
print(len(fruits))      # 6

list_A = [
    [1, 2, 3],
    ["www", "eeeee"]
]
print(list_A[0][0])     # 1





# Day 5: Loops
fruits = ["apple", "peach", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

for number in range(1, 3):       # 1, 2  (1 in included, 3 is not)
    print(number)

for digit in range(0, 5):       # 0,1,2,3,4
    print(digit)

for index in range(1, 10, 3):       # 1, 4, 7  (last number defines the step, the upper limit is not included)
    print(index)

# Count the sum of 1 + 2 + 3 + ... + 99 + 100:
total = 0
for number in range(1, 101):
    total += number
print(total)


