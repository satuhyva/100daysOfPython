############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# i ei koskaan saavuta arvoa 20, se looppaa 1...19
# korjaus: for i in range(1, 19):



# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# IndexError: list index out of range
# randint antaa koko välin numeroita, tässä 1...6, ja dice_imgs sisältää vain indeksit 0...6
# korjaus:  dice_num = randint(0, 5)


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# Ei anna vastausta kaikilla vuosiluvuilla, kuten esim. alle 1980 tai tasan 1994.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# puuttuu indentation

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))   # tässä on == eikä =
# total_words = pages * word_per_page
# print(total_words)
# word_per_page ei olekaan  input-numero, vaan se on conditional !!!

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# # b_list.append(new_item) ei ole sisennetty, siksi vain viimeinen numero tulee lisättyä

# mutate([1,2,3,5,8,13])