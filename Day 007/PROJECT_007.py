import random
import hangman_art
import hangman_words
import os


# word_list = hangman_words.word_list      
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list).upper()
displayed = []
for index in range(0, len(chosen_word)):
    displayed.append('_')

def print_view(lives_left, info_text, displayed_text):
    clear_console()
    print(hangman_art.logo) 
    print(' '.join(displayed_text))
    print(hangman_art.stages[lives_left])
    print(info_text)

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

game_over = False
lives = 6
info = ''

while not game_over:
    print_view(lives, info, displayed)
    guess = input("Guess a letter:\n").upper()
    found = False
    for index in range(0,len(chosen_word)):
        if guess == chosen_word[index]:
            found = True
            displayed[index] = guess
            info = f'The letter "{guess}" is in the word.'
    if not found:
        info = f'The letter "{guess}" is not in the word.'
        lives -= 1
        if lives == 0:
            print_view(lives, info, displayed)
            print('\nYOU LOSE!')
            game_over = True
    
    if not '_' in displayed:
        game_over = True
        print_view(lives, info, displayed)
        print('\nYOU WIN!')

