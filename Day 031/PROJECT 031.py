from tkinter import *
import csv
import random



BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 24, "bold")
STATUS_TEXT = ("Arial", 18)

word_pairs_learning_indexes = []
translated_words = []
current_pair_index = 0
learned_words = 0
missed_words = 0
change_counts_allowed = False


with open("translations.csv") as data_file:
    data = csv.reader(data_file)
    for line in data:
        russian = line[0]
        finnish = line[1].lower()
        if finnish != "FINNISH":
            translated_words.append({ "russian": russian, "finnish": finnish })


def get_new_word_pair():
    global current_pair_index
    global word_pairs_learning_indexes
    while True:
        random_number = random.randint(0, len(translated_words))
        if random_number not in word_pairs_learning_indexes:
            current_pair_index = len(word_pairs_learning_indexes)
            word_pairs_learning_indexes.append(random_number)
            return translated_words[random_number]


def show_next_word_pair():
    global flip_timer, change_counts_allowed
    change_counts_allowed = False
    window.after_cancel(flip_timer)
    new_word_pair = get_new_word_pair()
    canvas.itemconfig(language_label, text="RUSSIAN", fill="black")
    canvas.itemconfig(word_label, text=new_word_pair["russian"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)
    canvas.itemconfig(missed_label, text=f"missed: {missed_words}", fill="black")
    canvas.itemconfig(learned_label, text=f"learned: {learned_words}", fill="black")


def flip_card():
    global current_pair_index, word_pairs_learning_indexes, change_counts_allowed
    change_counts_allowed = True
    correct_answer = translated_words[word_pairs_learning_indexes[current_pair_index]]["finnish"]
    canvas.itemconfig(language_label, text="FINNISH", fill="white")
    canvas.itemconfig(word_label, text=correct_answer, fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(missed_label, text=f"missed: {missed_words}", fill="white")
    canvas.itemconfig(learned_label, text=f"learned: {learned_words}", fill="white")


def yes_button_pressed():
    global current_pair_index, word_pairs_learning_indexes, learned_words, translated_words
    learned_words += 1
    del translated_words[word_pairs_learning_indexes[current_pair_index]]
    show_next_word_pair()


def no_button_pressed():
    global current_pair_index, word_pairs_learning_indexes, missed_words, translated_words
    missed_words += 1
    show_next_word_pair()




window = Tk()
window.title("OPI VENÄJÄÄ")
window.config(padx=25, pady=10, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=400, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(200, 200, image=card_front)
canvas.grid(column=0, row=0, columnspan=3, rowspan=2)

language_label = canvas.create_text(200, 100, text="title", font=LANGUAGE_FONT)
word_label = canvas.create_text(200, 150, text="word", font=WORD_FONT)

learned_label = canvas.create_text(200, 220, text="", font=STATUS_TEXT)
missed_label = canvas.create_text(200, 240, text="", font=STATUS_TEXT)


no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=no_button_pressed)
no_button.grid(column=0, row=3)

yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=yes_button_pressed)
yes_button.grid(column=2, row=3)

show_next_word_pair()




window.mainloop()

