from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(padx=20, pady=30, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.score_label = Label(text="SCORE: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(150, 100, text="QUESTION", width=250, font=("Arial", 18, "bold"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.guessed_true)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.guessed_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"SCORE: {self.quiz_brain.score}")
            next = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=next)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end!\nYour score: {self.quiz_brain.score} / 10.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guessed_true(self):
        is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback(is_correct)


    def guessed_false(self):
        is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, answer_is_correct):
        if answer_is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




