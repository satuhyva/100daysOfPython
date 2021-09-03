from turtle import Turtle

DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.left(90)
        self.setx(0)
        self.sety(-280)

    def move(self):
        self.forward(DISTANCE)

    def reset_player(self):
        self.goto(0, -280)


