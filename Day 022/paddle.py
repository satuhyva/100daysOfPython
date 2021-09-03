from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.paddle = self.create_paddle(side)

    @staticmethod
    def create_paddle(side):
        bit = Turtle(shape="square")
        bit.shapesize(stretch_wid=5, stretch_len=1)
        bit.color("white")
        bit.penup()
        if side == "left":
            bit.setx(-380)
        else:
            bit.setx(380)
        bit.sety(0)
        return bit

    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)

    def get_y(self):
        return self.paddle.ycor()


