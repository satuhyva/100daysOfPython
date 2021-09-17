# DAY 6:

## While
index = 0
while index < 5:
    print(index)
    index += 1


## Functions
len("HUHUU")
print("HUHUU")
int("5")

def some_function():
    print("line 1")
    print("line 2")
    print("\n")

some_function()





# DAY 7:
import random
print(random.choice(["apple", "orange", "cherry"]))

import os
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)




# DAY 8:
## named parameters in functions
def named_animal(name_of_animal):
    print(name_of_animal)
named_animal(name_of_animal="Musti")

direction = "encode"
multiplier = (-1, 1)[direction == "encode"]
print(multiplier)                                   # 1

# join
print(" OR ".join(["apple", "orange", "cherry"]))     # apple OR orange OR cherry






# DAY 9:

## Dictionaries:
programmincg_terms = {
    "Bug": "kinda error",
    "Function": "callable piece of code",
     }
print(programmincg_terms["Bug"])                        # kinda error
programmincg_terms["Bug"] = "CHANGED"
print(programmincg_terms["Bug"])                        # CHANGED
for key in programmincg_terms:
    print(key)






# DAY 10:

## Functions with return values
def format_name(first, second):
    # .title()  capitalizes first letter
    return first.title() + ' ' + second.title()
print(format_name('angela', 'yu'))

## DOCSTINGS: text surrounded by """ and """
def some_other_function(input_text):
    """
    This function prints the input that it is given.
    Note: this docstring can contain several lines!
    Now HOVER OVER the function name!
    """
    print(input_text)

some_other_function('DOCSTRINGS ARE COOL!')



















