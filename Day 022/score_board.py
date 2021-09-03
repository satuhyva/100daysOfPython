from turtle import Turtle

FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-380, 270)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def increase(self):
        self.level += 1
        self.update_score_board()

    def show_game_over(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"GAME OVER! You reached level: {self.level}", False, align="center", font=FONT)

