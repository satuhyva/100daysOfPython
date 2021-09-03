from turtle import Turtle

FONT = ("Arial", 26, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"{self.score_left} | {self.score_right}", False, align="center", font=FONT)

    def increase(self, player):
        if player == "left":
            self.score_left += 1
        else:
            self.score_right += 1
        self.update_score_board()

    def show_game_over(self):
        self.goto(0, 0)
        winner = "LEFT player wins!"
        if self.score_left < self.score_right:
            winner = "RIGHT player wins!"
        if self.score_left == self.score_right:
            winner = "IT'S A DRAW!"
        self.write(winner, False, align="center", font=FONT)