import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\venki\OneDrive\Documents\Statistics\Statistics3.xlsx", index_col= 0 )
#print(df)
#print(df.describe())

q1 = df.Height.quantile(0.25)
q3 = df.Height.quantile(0.75)

iqr = q3-q1

print(iqr)
print(df.describe())

lower_limit = q1 - 1.5 * iqr
higher_limit = q3 + 1.5 * iqr

#print(lower_limit)
#print(higher_limit)

no_outliers = df[(df.Height >= lower_limit) & (df.Height <= higher_limit)]
outliers = df[(df.Height <= lower_limit) | (df.Height >= higher_limit)]
print(outliers)
print(no_outliers)

#print(q1)
#print(q3)
