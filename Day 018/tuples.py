# tuple on esim:
mun_tuple = (1, 6, 8)


# lista on esim:
mun_lista = [1, 2, 4]

print(mun_tuple[2])  # 8
print(mun_lista[2])  # 4

# ero?
# tuplen arvoja ei voi muuttaa!!!

import random


def get_pencolor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)
