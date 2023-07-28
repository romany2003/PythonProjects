import csv
import pandas as pd

data = pd.read_csv("Squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data['Primary Fur Color']


gray = len(data[data['Primary Fur Color']=="Gray"])
red = len(data[data['Primary Fur Color']=="Cinnamon"])
black = len(data[data['Primary Fur Color']=="Black"])

data_dict = {
    'Fur color': ['Gray', "cinnamon", "Black"],
    'count': [gray, red, black],
}

df = pd.DataFrame(data_dict)

df.to_csv('Squirrel_census/data.csv')