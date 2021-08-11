fruits = ["apple", "orange", "cherry", "pear"]

print(fruits[0])    # apple
print(fruits[-1])   # pear

fruits[-3] = "coconut"
print(fruits[1])    # coconut

fruits.extend(["banana", "plum"])
print(fruits[4])    # banana


print(len(fruits))      # 6


list_A = [
    [1,2,3],
    ["www", "eeeee"]
]

print(list_A[0][0])     # 1