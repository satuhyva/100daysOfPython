from turtle import Screen
import time

from player import Player
from highway import Highway
from car_manager import CarManager
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("TURTLE CROSSING")
screen.tracer(0)
player = Player()
highway = Highway()
highway.create_highway()
car_manager = CarManager()
score_board = ScoreBoard()
screen.onkeypress(player.move, "Up")
screen.listen()


sleep_time = 0.1
game_is_on = True

while game_is_on:
    time.sleep(sleep_time)
    if player.ycor() > 280:
        score_board.increase()
        car_manager.reset_cars()
        player.reset_player()
        time.sleep(3)
        sleep_time *= 0.75
    was_hit_by_car = car_manager.detect_hits(player)
    if was_hit_by_car:
        game_is_on = False
        score_board.show_game_over()
    car_manager.move_cars()
    car_manager.return_cars()
    screen.update()

screen.exitonclick()

