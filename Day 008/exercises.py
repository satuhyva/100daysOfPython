import math
# height = float(input("What is the wall height (m)? "))
# width = float(input("What is the wall width (m)? "))

# def calculatePaintNeed(width, height):
#     area = width * height
#     areaPerCan = 5.0
#     return area / areaPerCan

# paintNeed = calculatePaintNeed(width=width, height=height)
# print(f"You need {paintNeed} cans of paint, so buy {math.ceil(paintNeed)}.")







#Write your code below this line 👇

def prime_checker(number):
    for anotherNumber in range(2, number):
        print(anotherNumber)
        if number % anotherNumber == 0:
            print(f"Number {number} is NOT a prime number.") 
            return
    print(f"Number {number} is a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)