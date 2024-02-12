import pandas as pd
import numpy as np


df = pd.read_excel(r"C:\Users\venki\OneDrive\Documents\working.xlsx")
data = df.Income.quantile(0.99)
high_data = df[df.Income >= data]
print(high_data)
   
#print(df)
#df1 = df.Income.quantile(0.25, interpolation="lower")
#print(df1)

#data = df.Income.quantile(0.99)


#high_data = df[df.Income >= data]

#Remaining_data = df[df.Income < data]   

#print("Highest Value is")
#print(high_data)
#print("Remaining values")
#print(Remaining_data)
#print(df.describe())



#print(data)