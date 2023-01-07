#Find average mileage of each car company

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
Manufacturers_name = df.groupby('company')
res = Manufacturers_name['company','average-mileage'].mean()
print(res)