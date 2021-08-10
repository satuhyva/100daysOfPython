## DATA TYPES

# String
"HUHUU!"
"01234"[0]  
print("01234"[0])           # "0"
print("01234"[1])           # "1"
print("22" + "33")          # "2233"



# Integer
666
print(666)                  # 666
print(22 + 33)              # 55
print(1_000_000)            # 1000000


# Float
3.14


# Boolean
True
False


# What type?
numberOfCharacters = len(input("Your name? "))
print(type(numberOfCharacters))

# Type casting or conversion:
numberOfCakes = 5
numberAsString = str(numberOfCakes)
print("There are " + numberAsString + " cakes.")
a = 123         # int
str(a)          # string
b = float(123)  
print(b)        # 123.0
t = "223.5"
print(float(t) + " is a float")
