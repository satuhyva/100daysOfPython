from turtle import Turtle, Screen
# import turtle
# DO NOT use the following:
# from turtle import *
# will be difficult to know, where all stuff came from in code
# from turtle import Turtle as SlowAnimal

def draw_square(turtle, size):
    for index in range(0, 4):
        turtle.forward(size)
        turtle.left(90)

def draw_dashed_line(turtle, size):
    for index in range(0, 50):
        turtle.forward(size)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()


timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")

draw_square(timmy, 100)
timmy.penup()
timmy.right(90)
timmy.penup()
timmy.forward(100)
timmy.left(90)
draw_dashed_line(timmy, 3)

screen = Screen()
screen.exitonclick()