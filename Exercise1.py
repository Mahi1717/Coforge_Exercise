# Clean the dataset & update the CSV file
#Replace all column values which contain ?, NA etc.

import pandas as pd

#Assuming we are dealing with numeric fields only, we will be replacing NA values with 0, 
# we can also replace it with mean according to problem statement

df = pd.read_csv("Automobile_data.csv", na_values=(["?","NA"]))
df[["price", "average-mileage", "horsepower"]] = df[["price", "average-mileage", "horsepower"]].fillna(0)

print (df)
df.to_csv("Automobile_data.csv")
