from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("MUN GUI")
window.minsize(width=500, height=400)

#my_label = Label(text="LABEL TEXT", font=("Arial", 24, "bold"))
# my_label.pack(side="left")        # keskellä vasenta laitaa
#my_label.place(x=5, y=50)           # vasen ylänurkka on 0, 0; alaspäin on y kasvaa, oikealle x kasvaa

label_A = Label(text="LABEL A", font=("Arial", 14, "bold"))
label_B = Label(text="LABEL B", font=("Arial", 14, "bold"))
label_C = Label(text="LABEL C", font=("Arial", 14, "bold"))
label_D = Label(text="LABEL D..........", font=("Arial", 14, "bold"))
label_E = Label(text="LABEL E", font=("Arial", 14, "bold"))
label_A.grid(column=1, row=1)
label_B.grid(column=1, row=2)
label_C.grid(column=5, row=3)   # ei ole vielä column 5, joten siksi tulee columniin 3
label_D.grid(column=2, row=1)
label_E.grid(column=2, row=2)

# pack() ja grid() ei voi olla samassa tiedostossa!!!!

def button_pressed():
    print("Button pressed!")
    label_A["text"] = "X"


button = Button(text="PRESS", command=button_pressed)
button.grid(column=2, row=3)










# pitää ikkunan auki
window.mainloop()

