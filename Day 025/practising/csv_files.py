

#with open("data.csv", mode="r") as data_file:
    #data = data_file.readlines()
    #print(data)

import csv

with open("data.csv") as data_file:
    data = csv.reader(data_file)    # luo objektin
    temperatures = []
    for line in data:
        if line[1] not in temperatures and not line[1] == "temp":
            temperatures.append(int(line[1]))
        print(line)
    print(temperatures)


import pandas

weather_data = pandas.read_csv("data.csv")
print(weather_data)
print(weather_data["temp"])

print(type(weather_data))           # DataFrame     = whole table
print(type(weather_data["temp"]))   # Series        = single column

weather_dict = weather_data.to_dict()
print(weather_dict)
print(weather_data["day"])
print(weather_data["day"].tolist())

average= weather_data["temp"].mean()
print(f"{average:.1f}")
print(weather_data["temp"].max())

print(weather_data.condition)  # == weather_data["condition"]

print(weather_data[weather_data["day"] == "Mon"])
print(weather_data[weather_data.temp == weather_data.temp.max()])
monday = weather_data[weather_data["day"] == "Mon"]
print(monday)
print(monday.condition)


data_dict = {
    "students": ["Amy", "Stuart", "Angela"],
    "scores": [55, 77, 34]
}

data_1 = pandas.DataFrame(data_dict)
print(data_1)
data_1.to_csv("dict_to_csv")

# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw




