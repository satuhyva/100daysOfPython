from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()


def fw():
    timmy.forward(5)


def rev():
    timmy.backward(5)


def clock():
    timmy.right(5)
    timmy.forward(5)


def counter():
    timmy.left(5)
    timmy.forward(5)


def clear():
    timmy.clear()


screen.onkey(key="space", fun=fw)
screen.onkey(key="w", fun=fw)
screen.onkey(key="s", fun=rev)
screen.onkey(key="a", fun=clock)
screen.onkey(key="d", fun=counter)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
