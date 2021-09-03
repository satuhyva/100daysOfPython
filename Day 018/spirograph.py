from turtle import Turtle, Screen
import tuples


def draw_circle(turtle, size):
    turtle.pencolor(tuples.get_pencolor())
    turtle.circle(size, 360)
    turtle.right(4)


screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")
timmy.speed(0)

for index in range(0, 90):
    draw_circle(timmy, 100)


screen.exitonclick()
