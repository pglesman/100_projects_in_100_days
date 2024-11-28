import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241015.csv")

# turn created series from value_counts to Data Frame object
new_data = pandas.DataFrame(data["Primary Fur Color"].value_counts())
# reset index to create first column with index
new_data_reset = new_data.reset_index()
# create csv file of this data
new_data_reset.to_csv("squirrel_count.csv")
