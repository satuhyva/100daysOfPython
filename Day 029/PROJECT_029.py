from tkinter import *
from tkinter import messagebox
import pyperclip
from generage_password import generate_random_password


### CONSTANTS:
BACKGROUND = "#F6F6F6"
LABEL_FONT = ("Arial", 14, "bold")
SPACING = 5





### FUNCTIONALITY:
def save_password_to_file():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Do not leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(message=f"Website:\n{website}\n\n Username/Email:\n{username}\n\nPassword:\n{password}")
    if is_ok:
        with open("password_keeper.txt", mode="a") as file:
            file.write(f"{website} | {username} | {password}\n")
        website_input.delete(0, END)
        website_input.delete(0, END)
        password_input.delete(0, END)
    pyperclip.copy(password)

def generate_password_automatically():
    generated_password = generate_random_password()
    password_input.delete(0, END)
    password_input.insert(0, generated_password)



### GUI:
window = Tk()
window.title("PASSWORD KEEPER")
window.config(padx=25, pady=10, bg=BACKGROUND)

logo = PhotoImage(file="lock.png")
canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=LABEL_FONT, bg=BACKGROUND)
website_label.grid(column=0, row=1)
website_input = Entry(width=30, highlightthickness=0)
website_input.grid(column=1, row=1, columnspan=2, padx=SPACING, pady=SPACING)
website_input.focus()

username_label = Label(text="Username/Email:", font=LABEL_FONT, bg=BACKGROUND)
username_label.grid(column=0, row=2)
username_input = Entry(width=30, highlightthickness=0)
username_input.insert(0, "my.email@somemail.com")
username_input.grid(column=1, row=2, columnspan=2, padx=SPACING, pady=SPACING)

password_label = Label(text="Password:", font=LABEL_FONT, bg=BACKGROUND)
password_label.grid(column=0, row=3)
password_input = Entry(width=30, highlightthickness=0)
password_input.grid(column=1, row=3, columnspan=2, padx=SPACING, pady=SPACING)

password_button = Button(text="GENERATE PASSWORD", highlightthickness=0, command=generate_password_automatically)
password_button.grid(column=1, row=4, padx=SPACING, pady=SPACING)

store_button = Button(text="SAVE PASSWORD", highlightthickness=0, command=save_password_to_file)
store_button.grid(column=1, row=5, padx=SPACING, pady=SPACING)




window.mainloop()