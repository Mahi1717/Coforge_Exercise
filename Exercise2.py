#Find the most expensive car company name

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
print(df)