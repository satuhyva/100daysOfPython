# FileNotFoundError
# with open("non_existent.txt") as file:
    # file.readlines()

# KeyError
# fruits = { "key": "value"}
# print(fruits["apple"])

# IndexError
# list = [1,2,3]
# print(list[22])

# TypeError
# text = "333"
# print(text + 333)



try:
    # tehdään jotain, mikä voi mennä pieleen
    file = open("non_existent.txt")
    #print('333' + 333)
# kun on except ilman virhetyyppiä, KAIKKI muodostuvat errorit tulee tänne yo.try-lohkosta (ellei määrätty, mikä virhe)
except FileNotFoundError as file_error:
    # mitä tehdään, jos jotain menee pieleen (tulee exception)
    print(f"ERROR in file: {file_error}")
    file = open("non_existent.txt", mode="w")
except TypeError:
    print("type error")

else:
    # jos ei tulee exceptionia
    content = file.read()
    print(content)

finally:
    # tehdään riippumatta siitä, onnistuuko
    file.close()
    print("DONE!")
    #raise KeyError("oma viesti")
    #raise TypeError("joku viesti")



height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 2.5:
    raise ValueError("Ei voi olla niin pitkä ihminen!")

bmi = weight / height ** 2
print(f"{bmi:.2f}")














