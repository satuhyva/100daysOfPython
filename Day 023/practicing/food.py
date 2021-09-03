from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed("fastest")
        x = random.randint(-14, 14)
        y = random.randint(-14, 14)
        self.goto(x * 20, y * 20)

    def refresh(self):
        x = random.randint(-14, 14)
        y = random.randint(-14, 14)
        self.goto(x * 20, y * 20)


