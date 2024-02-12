import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\venki\OneDrive\Documents\working2.xlsx")

#df["Income"][2] = np.nan

#@print(df)

new_data = df.fillna(df.Income.median()) 

print(new_data)

#print(df.describe())

