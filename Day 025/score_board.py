from turtle import Turtle

FONT = ("Arial", 20, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Correct answers: {self.score}", False, align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update_score_board()

    def show_game_over(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"   GAME OVER! \nYou got: {self.score} / 50 right.", False, align="center", font=FONT)

