# maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()


# #
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    
# while not at_goal():
#     turn_left()
#     if front_is_clear():
#         move()
#     else:
#         turn_right()
#         if front_is_clear():
#             move()
#         else:
#             turn_right()
#             if front_is_clear():
#                 move()



# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

    
# while not at_goal():
#     if wall_on_right():
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#             if front_is_clear():
#                 move()
#     else:
#         turn_right()
#         move()
