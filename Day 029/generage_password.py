import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 8
nr_numbers = 6
nr_symbols = 4


def generate_random_password():
    characters = []
    characters += [letters[random.randint(0, len(letters) - 1)] for _ in range(0, nr_letters)]
    characters += [numbers[random.randint(0, len(numbers) - 1)] for _ in range(0, nr_numbers)]
    characters += [symbols[random.randint(0, len(symbols) - 1)] for _ in range(0, nr_symbols)]
    random.shuffle(characters)
    return "".join(characters)
