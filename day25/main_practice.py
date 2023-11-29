import pandas
# weather_list = []
# with open("weather_data.csv") as weather_date:
#     weather_list.append(weather_date.read().splitlines())
# print(weather_list)

# import csv
#
# temp = []
# with open("weather_data.csv") as weather_date:
#     data = csv.reader(weather_date)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
# print(temp)


# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)

# temp = data["temp"].tolist()
# print(sum(temp)/len(temp))

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp*9/5 +32)

# dataframe from scratch
# data_dict = {
#     "studants" : ["Amy", "Sarah", "Mak"],
#     "scores": [98, 87, 43]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data[data["Primary Fur Color"] == 'Gray'])
red = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black = len(data[data["Primary Fur Color"] == 'Black'])
data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}
# fur = data["Primary Fur Color"].tolist()
# for color in fur:
#     if color == 'Gray':
#         data_dict["Count"][0] += 1
#     elif color == 'Cinnamon':
#         data_dict["Count"][1] += 1
#     elif color == 'Black':
#         data_dict["Count"][2] += 1
pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")
