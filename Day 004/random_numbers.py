import random
# importing data from another file:
import extra_data

random_number = random.randint(1,10)
print(random_number)

# importing data from another file:
print(extra_data.my_constant)

# Random number between 0.0 and 1.0. 0.0 IS included, 1.0 is not! 0.0 - 0.999999.....
print(random.random())

random_float = random.random()
# To get random numbers between 0.0 - 5:
print(random_float * 5)