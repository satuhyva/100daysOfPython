alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    crypted = []
    multiplier = (-1, 1)[direction == 'encode']
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            newIndex = index + shift * multiplier
            # if newIndex > len(alphabet) - 1:
            #     newIndex -= len(alphabet)
            # if newIndex < 0:
            #     newIndex += len(alphabet)
            crypted.append(alphabet[newIndex])
        else:
            crypted.append(letter)
    return "".join(crypted)  

def directionIsOK(direction):
    return direction == 'encode' or direction == 'decode'




while (True):

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    if not (direction == 'encode' or direction == 'decode'):
        print(f"Direction must be 'encode' or 'decode', {direction} is not ok.\n")
        continue

    text = input("Type your message:\n").lower()


    shift = int(input("Type the shift number:\n"))
    if not (0 < shift < len(alphabet)):
        print(f"Shift must be a number between 1 and {len(alphabet)}. {shift} is not OK.\n")
        continue

    crypted = caesar(text, shift, direction)
    print(f"The {direction}d result is: {crypted}")
    nextMove = input("Type 'yes' to go again. \n")
    if nextMove != 'yes':
        break
    else:
        print("Goodbye!")
