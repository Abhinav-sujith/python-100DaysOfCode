# with open("weather_data.csv",'r') as data:
#     weather = data.readlines()
#     print(weather)

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas as pd
data = pd.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
#print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# mean = sum(temp_list)/len(temp_list)
# print(mean)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].quantile()) # This will work more like series
# print(data.condition) # This is more like an object

# print(data[data["temp"] == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday.temp)
#
# fahrenheit = (monday.temp[0] * 9/5) + 32
# print(fahrenheit)
#
# data_dictionary = {
#     "students" : ["Amy","Abhi", "Alex"],
#     "score" : [90,99,98]
# }
#
# data = pd.DataFrame(data_dictionary)
# data.to_csv("new_data.csv")


df = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")
squirrel = df.groupby("Primary Fur Color")["Primary Fur Color"].count()





















