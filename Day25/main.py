# # with open("weather_data.csv", "r") as weather_data:
# #     weather_data_list = weather_data.readlines()

# # print (weather_data_list)

# # import csv

# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #         print(row)
    
# #     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# # data_dict = data.to_dict()
# # print(data_dict)

# # data_list = data["temp"].to_list()
# # print(data["temp"].max())

# #get data in row
# print(data[data.temp == data["temp"].max()])

# # monday = data[data.day == "Monday"]
# # print(monday.condition)

# print((data["temp"]*(9/5))+32)

# #Create a datafram from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")


