# my_file = open("data.txt")
# contents = my_file.read()
# print(contents)
# my_file.close()

# automaattisesti sulkee tiedoston lopussa
with open("data.txt") as my_file:
    contents = my_file.read()
    print(contents)

# read on moden default
with open("data.txt", mode="w") as my_file_again:
    my_file_again.write("Content changed to this.\n")

with open("data.txt") as my_file:
    contents = my_file.read()
    print(contents)

with open("data.txt", mode="a") as my_file_third_time:
    my_file_third_time.write("Append this line to content.")

with open("data.txt") as my_file:
    contents = my_file.read()
    print(contents)

with open("non_existent.txt", mode="w") as some_file:
    some_file.write("Write a line to a file that does not yet exist.")

with open("non_existent.txt") as my_file:
    contents = my_file.read()
    print(contents)
