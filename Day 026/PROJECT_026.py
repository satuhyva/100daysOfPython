import pandas

codes = pandas.read_csv("nato.txt")
codes_dict = { row.letter: row.code for (index, row) in codes.iterrows() }


word = input("Enter a word: ")
letters = [codes_dict[letter.upper()] for letter in word]
toPrint = ""
for item in letters:
    toPrint += item + ", "
toPrint = toPrint[0:len(toPrint) - 2]
print(toPrint)

