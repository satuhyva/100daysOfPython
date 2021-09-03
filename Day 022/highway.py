from turtle import Turtle


class Highway(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.pensize(5)
        self.penup()
        self.hideturtle()

    def create_highway(self):
        self.goto(-380, -260)
        self.pendown()
        self.goto(380, -260)
        self.penup()
        self.goto(380, 260)
        self.pendown()
        self.goto(-380, 260)
        self.penup()

