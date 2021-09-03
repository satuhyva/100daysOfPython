from turtle import Turtle

FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update_score_board()

    def show_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align="center", font=FONT)