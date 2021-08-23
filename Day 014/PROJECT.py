import game_data
import random


def comparison(a, b):
    return a["follower_count"] > b["follower_count"]

print("WELCOME TO HIGHER LOWER GAME")

options_count = len(game_data.data)

option_a = None
correct_count = 0

while True:
    if option_a == None: 
        option_a = random.choice(game_data.data)
        correct_count = 0
    option_b = random.choice(game_data.data)
    while option_b == option_a:
        option_b = random.choice(game_data.data)
    print(f'A: {option_a["name"]} ')
    print("   vs.")
    print(f'B: {option_b["name"]} ')

    answer = input("Which one has more followers, A or B? ")
    answerIsCorrent = comparison(
        (option_b, option_a)[answer.lower() == 'a'],
        (option_a, option_b)[answer.lower() == 'a']
    )
    if (answerIsCorrent):
        correct_count += 1
        print(f"You are right! Current score is: {correct_count}.")
    else:
        print(f"Sorry, wrong answer! Your final score is: {correct_count}.")
        another_game = input("Want to go again (y or n)? ")
        if another_game == 'n':
            break
    option_a = option_b


