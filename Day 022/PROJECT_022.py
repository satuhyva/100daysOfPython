from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
score_board = ScoreBoard()

screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_is_on = True
sleep_time = 0.05

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if score_board.score_left + score_board.score_right == 10:
        game_is_on = False
        score_board.show_game_over()
    if ball.xcor() >= 360:
        paddle_top_y = right_paddle.get_y() + 100 * 0.5
        paddle_bottom_y = right_paddle.get_y() - 100 * 0.5
        if paddle_bottom_y <= ball.ycor() <= paddle_top_y:
            ball.turn()
            score_board.increase("right")
            sleep_time *= 0.85
        elif ball.xcor() >= 420:
            ball.reset("left")
            sleep_time = 0.05
            screen.update()
            time.sleep(2)
    if ball.xcor() <= -360:
        paddle_top_y = left_paddle.get_y() + 100 * 0.5
        paddle_bottom_y = left_paddle.get_y() - 100 * 0.5
        if paddle_bottom_y <= ball.ycor() <= paddle_top_y:
            ball.turn()
            score_board.increase("left")
            sleep_time *= 0.85
        elif ball.xcor() <= -420:
            ball.reset("right")
            sleep_time = 0.05
            screen.update()
            time.sleep(2)
    ball.move()




screen.exitonclick()


