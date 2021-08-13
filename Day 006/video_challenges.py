# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# HURDLE 1:
def turn_right():
    turn_left()
    turn_left()
    turn_left()   


    
def move_over_wall():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for index in range(0,6):
    move_over_wall()

# OR:
# index = 0
# while index < 6:
#     move_over_wall()
#     index += 1

# OR:
# while not at_goal():
#     move_over_wall()



# HURDLE 3:
def turn_right():
    turn_left()
    turn_left()
    turn_left()   

def climb_over_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        climb_over_wall()
    else:
        move()


#


# HURDLE 4:
def turn_right():
    turn_left()
    turn_left()
    turn_left()   

def climb_over_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        climb_over_wall()
    else:
        move()




        