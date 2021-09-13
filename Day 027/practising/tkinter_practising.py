from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("MUN GUI")
window.minsize(width=500, height=400)

my_label = Label(text="LABEL TEXT", font=("Arial", 24, "bold"))
my_label.pack()         # asettaa keskelle ylös
#my_label.pack(side="left")  # asettaa keskelle vasemmalle

my_label2 = Label(text="LABEL TEXT 2", font=("Arial", 24, "bold"))
my_label2.pack()

def button_pressed():
    print("Button pressed!")
    my_label["text"] = "Button pressed!"


button = Button(text="PRESS", command=button_pressed)
button.pack()
# http://tcl.tk/man/tcl8.6/TclCmd/contents.htm, https://www.tcl.tk/man/tcl8.4/TkCmd/entry.html
# https://www.tcl.tk/man/tcl8.4/TkCmd/
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html


input = Entry(width=10)
input.pack()


def button2_pressed():
    print("Button 2 pressed!")
    my_label2["text"] = "Button 2 pressed!"
    print(input.get())

button2 = Button(text="PRESS", command=button2_pressed)
button2.pack()









# pitää ikkunan auki
window.mainloop()

