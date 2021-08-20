import random
print("\nWELCOME TO THE NUMBER GUESSING GAME")



def get_difficulty():
    difficulty_level = input("Choose a difficulty. Type e (easy) or h (hard): ")
    if difficulty_level != 'e' and difficulty_level != 'h':
        print("Difficulty must be either 'e' or 'h'!")
        get_difficulty()
    return difficulty_level

def get_next_guess(guesses_count):
    print(f"You have {guesses_count} attempts left.")
    guess_input = input(f"Your guess: ")
    if not guess_input.isdecimal():
        print("A guess must be a number!")
        get_next_guess(guesses_count)
    return int(guess_input)

def check_guess(correct_number, guessed_number):
    if correct_number == guessed_number:
        print("Correct!")
        return True
    if correct_number > guessed_number:
        print("Too low!")
        return False
    else:
        print("Too high!")
        return False



play_another_game = True

while play_another_game:
    print("Let's play!")
    difficulty = get_difficulty()
    the_number = random.randint(1,100)
    print("I am thinking of a number between 1 and 100. Try to guess it!")
    guesses = (5,10)[difficulty == 'e']
    
    while guesses > 0:
        next_guess = get_next_guess(guesses)
        guess_is_correct = check_guess(the_number, next_guess)
        if guess_is_correct:
            go_again = input("Do you want to go again (y or n)? ")
            if go_again == 'y':
                break
            else:
                play_another_game = False
                break
        guesses -= 1