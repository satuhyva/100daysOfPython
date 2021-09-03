from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("KÄÄRMEPELI")
screen.tracer(0)


snake = Snake()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.listen()

food = Food()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    snake.move()
    if snake.snake_bits[0].distance(food) < 15:
        snake.grow()
        score_board.increase()
        food.refresh()
    for bit in snake.snake_bits[1:]:
        if snake.snake_bits[0].distance(bit) < 10:
            game_is_on = False
            score_board.show_game_over()
    if not -300 < snake.snake_bits[0].xcor() < 300:
        game_is_on = False
        score_board.show_game_over()
        continue
    if not -300 < snake.snake_bits[0].ycor() < 300:
        game_is_on = False
        score_board.show_game_over()
        continue
    screen.update()
    time.sleep(0.4)

screen.exitonclick()
