# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("purple")
# timmy.forward(100)
#
#
# my_screen = Screen()
# my_screen.canvheight = 300
# my_screen.canvwidth = 300
#
# my_screen.exitonclick()

# adding external library to project:
# python packages  pypi
# https://pypi.org/project/prettytable/
# pycharm > preferences > project > interpreter > pip > +-button > prettytable > install

from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("POKEMON", ["Poliwag", "Pikachu"])
print(table)
table.add_column("TYPE", ["type 1", "type 2"])
print(table)
table.add_row(["Bulbasaur", "type 3"])
print(table)
table.align = 'l'
print(table)

