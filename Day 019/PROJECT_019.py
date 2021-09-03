from turtle import Turtle, Screen
import random

screen = Screen()
# does not work:
# screen.setup(width=100, height=800)


colors = ["blue", "green", "purple", "red", "lime"]

def create_turtle(i):
    turtle = Turtle(shape="turtle", visible=False)
    turtle.color(colors[i])
    turtle.penup()
    turtle.setx(0)
    turtle.sety(0 - i * 50)
    turtle.showturtle()
    return turtle

def move_turtle_random(turtle):
    speed = random.randint(0, 10)
    turtle.speed(speed)
    turtle.forward(speed)


turtles = []
for index in range(0, 5):
    turtles.append(create_turtle(index))

bet = screen.textinput(title="Winner color?", prompt="What color turtle will win? blue (b), green (g),\
  purple (p), red (r) or lime (l)?")

limit = 250
winner = -1
while winner == -1:
    for index in range(0, len(turtles)):
        move_turtle_random(turtles[index])
        distance = turtles[index].xcor()
        if distance > limit:
            winner = index
print(winner)

win = False
if bet == "b" and winner == 0:
    win = True
elif bet == "g" and winner == 1:
    win = True
elif bet == "p" and winner == 2:
    win = True
elif bet == "r" and winner == 3:
    win = True
elif bet == "l" and winner == 4:
    win = True

if win:
    turtles[winner].write("I won!", True, align="right", font=("Arial", 15, "normal"))
else:
    turtles[winner].write("I won! You did not guess that!", True, align="right", font=("Arial", 15, "normal"))

screen.exitonclick()



