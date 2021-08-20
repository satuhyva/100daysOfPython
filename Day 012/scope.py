enemies = 1
print(f"outside {enemies}")
def increase_enemies():             # TÄSSÄ luodaan uusi muuttuja enemies
    # enemies += 1                    # UnboundLocalError: local variable 'enemies' referenced before assignment
    enemies = 2                        # INSIDE 2
    print(f"INSIDE {enemies}")
increase_enemies()
print(f"outside {enemies}")         # outside 1


# LOCAL SCOPE:

def insider():
    inside_variable = 1
    print(inside_variable)     # 1

insider()
# print(insider_variable)     # undefined variable (before running)
# print(insider_variable)     # NameError: name 'insider_variable' is not defined (when running)


# GLOBAL SCOPE:
print('\nGLOBAL:')
player_health = 10
def drink_potion():
    print(f"IN: {player_health}")
    health = player_health * 2
    print(f"USED IN OTHER: {health}")
    # The following is not allowed:
    # player_health *= 2      
    # print(player_health)

drink_potion()
print(f"OUT: {player_health}")

# THERE IS NO BLOCK SCOPE
print("\n")
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)                # Skeleton (vaikka ollaan if-loopin ulkopuolella!!!)
                                # Eli IF-rakenteesta näkyy ulos, if, while, for, kaikista näkyy ulos

def create_new_enemy():
    if game_level < 5:
        another_new_enemy = enemies[1]
        print(f"IN: {another_new_enemy}")
create_new_enemy()
# print(f"OUT: {another_new_enemy}")    # mutta funktiosta ei!



# MODIFY GLOBAL
print("\nMODIFY GLOBAL")
potions = 5
print(potions)
def manufacture_global():
    global potions          # otetaan globaali käyttöön ja muutetaan sitä globaalisti
    potions += 3
manufacture_global()
print(potions)
def manufacture_return():
    return potions + 8      # palautetaan käyttöön globaalia muuntava
print(manufacture_return())


print("\nGLOBAL CONSTANTS")   # UPPERCASE NAMING (muistuttaa käytettäessä, ettei yritä muuttaa)
PI = 3.14

def calculate():
    print(PI)