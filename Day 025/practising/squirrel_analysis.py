import pandas

data = pandas.read_csv("squirrel.csv")
greys = len(data[data["Primary Fur Color"] == "Gray"])
cinnamons = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "colors": ["grey", "cinnamon", "black"],
    "counts": [greys, cinnamons, blacks]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_results.csv")

