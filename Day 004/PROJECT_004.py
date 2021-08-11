import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

computerChoice = random.choice([0, 1, 2])
print("Welcome to ROCK, PAPER AND SCISSORS!")
print("What is your choice?")
print(" 0 - ROCK")
print(" 1 - PAPER")
print(" 2 - SCISSORS")
playerChoice = int(input(""))

print("\n\nComputer choice:")
print(choices[computerChoice])
print("\n\nYour choice:")
print(choices[playerChoice])

if computerChoice == playerChoice:
  result = 'It is a draw.'
elif computerChoice == playerChoice + 1 or computerChoice == playerChoice - 2:
  result = "Computer wins!"
else:
  result = "You win!"

print(result)