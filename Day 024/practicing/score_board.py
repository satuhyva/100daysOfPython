from turtle import Turtle

FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_highest_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score_board()

    @staticmethod
    def get_highest_score():
        with open("highest_score.txt") as score_file:
            highest = int(score_file.read())
        return highest

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}. Highest score: {self.highest_score}", False, align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update_score_board()

    def set_highest_score(self):
        with open("highest_score.txt", mode="w") as score_file:
            score_file.write(str(self.score))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.set_highest_score()
        self.score = 0
        self.update_score_board()

    def show_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align="center", font=FONT)