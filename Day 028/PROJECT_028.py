from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
count_downs_performed = 0
CHECKS = ["", "✓", "✓✓", "✓✓✓", "✓✓✓✓"]



# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global count_downs_performed
    count_downs_performed = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global count_downs_performed
    if count_downs_performed in [0, 2, 4, 6]:
        count_down(WORK_MIN * 60)
        current_activity.config(text="TIME TO WORK!", fg=GREEN)
        checks.config(text=CHECKS[int(count_downs_performed / 2)])
    elif count_downs_performed in [1, 3, 5]:
        current_activity.config(text="SHORT  BREAK!", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif count_downs_performed == 7:
        current_activity.config(text="LOOONG BREAK!", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif count_downs_performed == 8:
        checks.config(text=CHECKS[int(count_downs_performed / 2)])
        current_activity.config(text="WELL DONE YOU!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global count_downs_performed
    minutes = math.floor(count / 60)
    seconds = count - minutes * 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count == -1:
        count_downs_performed += 1
        start_timer()
    else:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #

# https://colorhunt.co

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)  # padding kuvan ympärille



current_activity = Label(text="", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
current_activity.grid(column=2, row=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=photo)  # x, y, image

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

#count_down(5)

start_button = Button(text="START", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)

reset_button = Button(text="RESET", command=reset_timer,  highlightthickness=0)
reset_button.grid(column=3, row=3)

checks = Label(text="", font=("Arial", 20, "bold"), fg=GREEN, bg=YELLOW, pady=10)
checks.grid(column=2, row=3)



window.mainloop()
