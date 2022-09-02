# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("DBC.csv")
cities = ['Aka', 'Bethlehem', 'Dura', 'Haifa', 'Halhoul', 'Hebron', 'Jenin', 'Jericho', 'Jerusalem', 'Nablus', 'Nazareth', 'Qalqilya', 'Ramallah', 'Ramleh', 'Sabastia', 'Safad', 'Salfit', 'Tubas', 'Tulkarm', 'Yafa']

# updating the column value/data
# for city in cities:
#     for i in range(len(df[city])):
#         df[city][i] = df[city][i].replace(',', '+')

for city in cities:
    for i in range(len(df[city])):
        lis = df[city][i].split('+')
        if len(lis) == 2:
            df[city][i] = df[city][i] + '+10000'
        

# print(df["Aka"])

# writing into the file
df.to_csv("DBC.csv", index=False)

print(df)
