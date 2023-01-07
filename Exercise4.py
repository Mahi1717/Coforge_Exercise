#Find each company’s highest price car

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
Manufacturers_name = df.groupby('company')
res = Manufacturers_name['company','price'].max()
print(res)