# https://www.sporcle.com
# https://www.sporcle.com/games/g/states

import pandas
import turtle


import score_board

screen = turtle.Screen()
screen.title("US STATES")
states_img = "image.gif"
screen.addshape(states_img)
turtle.shape(states_img)
score_board = score_board.ScoreBoard()


states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].tolist()
guessed_states = []
screen.tracer(0)

while len(guessed_states) < 50:
    answer = screen.textinput(title="Guess a state", prompt="What is your guess for another US state?")
    if not answer:
        break
    answer = answer.title()
    if answer in all_states:
        if answer not in guessed_states:
            score_board.increase()
            guessed_states.append(answer)
            state_details = states_data[states_data["state"] == answer]
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.color("green")
            state_name.penup()
            state_name.goto(int(state_details.x), int(state_details.y))
            state_name.write(f"{answer}", False, align="center", font=("Arial", 12, "bold"))
            screen.update()

missing_states = []
for missed_state in all_states:
    if missed_state not in guessed_states:
        missing_states.append(missed_state)
        state_details = states_data[states_data["state"] == missed_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.color("red")
        state_name.penup()
        state_name.goto(int(state_details.x), int(state_details.y))
        state_name.write(f"{missed_state}", False, align="center", font=("Arial", 12, "bold"))
        screen.update()

missed_data = pandas.DataFrame(missing_states)
missed_data.to_csv("missed_states.csv")

score_board.show_game_over()
screen.update()

# def get_mouse_click_coordinates(x, y):
# print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)

# keeps window open
turtle.mainloop()

# screen.exitonclick()
