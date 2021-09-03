import colorgram
from turtle import Turtle, Screen
import random

hirst_colors = colorgram.extract('hirst.png', 10)


def create_color_list():
    color_list = []
    for index in range(0, 10):
        colorgram_color = hirst_colors[index].rgb
        color_list.append((colorgram_color.r, colorgram_color.g, colorgram_color.b))
    return color_list


colors = create_color_list()


def draw_dot(turtle):
    turtle.pendown()
    color = colors[random.randint(0, 9)]
    turtle.dot(80, color)
    turtle.penup()


def draw_row(turtle, size):
    for index in range(0, size):
        draw_dot(turtle)
        if index != size - 1:
            turtle.forward(100)


def move_up_a_row(turtle, direction):
    if direction == "right":
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    else:
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)


screen = Screen()
screen.colormode(255)

hirst = Turtle()
hirst.color("black")
hirst.pensize(50)
hirst.speed(1)
hirst.penup()
hirst.backward(400)
hirst.right(90)
hirst.forward(300)
hirst.left(90)


for row in range(0, 9):
    draw_row(hirst, 9)
    move_up_a_row(hirst, ("right", "left")[row % 2 != 0])


screen.exitonclick()
