from turtle import Turtle, Screen
import random
from tuples import get_pencolor


def redirect_and_walk(turtle, size):
    turtle.pencolor(get_pencolor())
    turns = random.randint(0, 3)
    angles = [90, 180, 270, 360]
    turtle.left(angles[turns])
    turtle.forward(size)

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")
timmy.pensize(20)
timmy.speed(10)
for times in range(0, 20):
    redirect_and_walk(timmy, 50)


screen.exitonclick()