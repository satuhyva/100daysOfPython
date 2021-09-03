from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "black", "lime", "rosybrown"]


def draw_shape(turtle, sides):
    angle = 360 / sides
    turtle.color(colors[sides])
    for index in range(0, sides):
        turtle.forward(100)
        turtle.right(angle)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")
for side_number in range(3, 10):
    draw_shape(timmy, side_number)

screen = Screen()
screen.exitonclick()
