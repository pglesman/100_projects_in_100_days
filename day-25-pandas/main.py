import pandas


def f(x):
    x = x * 1.8 + 32
    return float(x)


data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# convert to a dictionary
data_dict = data.to_dict()
print(data_dict)

# convert data to a list
temp_list = data["temp"].to_list()
print(temp_list)

# average temp in a series "temp" (series is a column in pandas)
aver_temp = data["temp"].mean()
print(aver_temp.round(2))

# max temp in a series "temp"
print(data["temp"].max())

# getting a row from a data
print(data[data.day == "Monday"])

# getting a specify row that holds max value
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

# getting a value from a specify cell
print(monday.condition)
print(monday.temp[0])

# applying a function to a specify row
print(monday["temp"].apply(f))

# creating a dataframe from a scratch
new_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 75, 65],
}
new_data = pandas.DataFrame(new_dict)
print(new_data)
data.to_csv("new_data.csv")