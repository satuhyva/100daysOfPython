original_list = [1, 2, 3, 4]
new_list = [item * 5 for item in original_list]
print(new_list)

original_name = "Angela"
name_as_list = [character.upper() for character in original_name]
print(name_as_list)

newly_created = [number * 2 for number in range(0, 5)]
print(newly_created)

if_list = [number * 10 for number in range(0, 10) if number % 2 != 0]
print(if_list)

long = ["Angela", "Bob", "Caroline", "Bill"]
short = [name for name in long if len(name) < 5]
print(short)


import random

scores = {name: random.randint(0, 10) for name in ["Mat", "Silvia", "George"]}
print(scores)
passed = { name: score for (name, score) in scores.items() if score > 5 }
print(passed)


import pandas
student_data = {
    "student": ["Angela", "Bob", "Bill"],
    "score": [22,33,44]
}
student_data_frame = pandas.DataFrame(student_data)
print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(key)      # key onkin column nimi eli ensin student, sitten toisella kierroksella score
    print(value)    # ja sitten tässä tulee values eli ensin student values, jotka on nimet, ja tokalla kiekalla numerot
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student, row.score)
    print("\n")
