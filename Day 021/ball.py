from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)
        self.change_in_x = 5
        self.change_in_y = 5 #* 600 / 800

    def move(self):
        if self.ycor() >= 285 or self.ycor() <= -285:
            self.change_in_y *= -1
        self.goto(self.xcor() + self.change_in_x, self.ycor() + self.change_in_y)

    def turn(self):
        self.change_in_x *= -1
        self.goto(self.xcor() + self.change_in_x, self.ycor() + self.change_in_y)

    def reset(self, direction):
        self.goto(0, 0)
        self.change_in_y = 5
        if direction == "left":
            self.change_in_x = -5
        else:
            self.change_in_x = 5

