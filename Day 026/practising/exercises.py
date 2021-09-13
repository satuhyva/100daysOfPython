numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number ** 2 for number in numbers]

#Write your code 👆 above:

print(squared_numbers)



numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result2 = [number for number in numbers2 if number % 2 == 0]

#Write your code 👆 above:

print(result2)


numbers1 = []
with open("file1.txt", mode="r") as file1:
    lines1 = file1.readlines()
    numbers1 = [int(line.replace("\n", "")) for line in lines1]
numbers2 = []
with open("file2.txt", mode="r") as file1:
    lines2 = file1.readlines()
    numbers2 = [int(line.replace("\n", "")) for line in lines2]

print(numbers1)
print(numbers2)
common = [number for number in numbers1 if number in numbers2]
print(common)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
letter_counts = {word: len(word) for word in sentence.replace("?", "").split(" ")}
print(letter_counts)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = { day : (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items() }
print(weather_f)