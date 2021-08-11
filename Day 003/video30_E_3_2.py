# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2

result = "underweight"
if bmi > 35:
  result = "clinically obese"
elif bmi > 30:
  result = "obese"
elif bmi > 25:
  result = "slightly overweight"
elif bmi > 18.5:
  result = "normal weight"

print(f"Your BMI is {int(bmi)}, you are {result}.")