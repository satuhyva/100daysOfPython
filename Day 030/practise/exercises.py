fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit with this index not available!")
    else:
        print(fruit + " pie")

make_pie(4)



facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        print("No likes at all")

print(total_likes)




import pandas

codes = pandas.read_csv("../nato.txt")
codes_dict = {row.letter: row.code for (index, row) in codes.iterrows()}

while True:
    word = input("Enter a word: ")
    print(word)
    try:
        letters = [codes_dict[letter.upper()] for letter in word]
        print(letters)
    except KeyError:
        print("Only letters in alphabet please!")
    else:
        break

toPrint = ""
for item in letters:
    toPrint += item + ", "
toPrint = toPrint[0:len(toPrint) - 2]
print(toPrint)


