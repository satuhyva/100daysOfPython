from tkinter import Tk, Label, Button, Entry, END

window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=500, height=400)

miles = Entry(width=10)
miles.insert(END, string="0")
miles.grid(column=2, row=1)
kilometers = Label(text="0")
kilometers.grid(column=2, row=2)


def convert():
    miles_given = int(miles.get())
    kilometers["text"] = str(miles_given * 1.60934)


miles_label = Label(text="miles")
miles_label.grid(column=3, row=1)

kilometers_label = Label(text="kilometers")
kilometers_label.grid(column=3, row=2)

equals_label = Label(text="is equal to")
equals_label.grid(column=1, row=2)

calculate_button = Button(text="calculate", command=convert)
calculate_button.grid(column=2, row=3)

window.mainloop()
