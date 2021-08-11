# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined = name1.upper() + name2.upper()

trueCount = 0
trueCount += combined.count("T")
trueCount += combined.count("R")
trueCount += combined.count("U")
trueCount += combined.count("E")

loveCount = 0
loveCount += combined.count("L")
loveCount += combined.count("O")
loveCount += combined.count("V")
loveCount += combined.count("E")

score = int(str(trueCount) + str(loveCount))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")