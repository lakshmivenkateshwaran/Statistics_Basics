from fastapi import FastAPI
import pandas as pd
from statistics_internal import session3

app = FastAPI()


df = pd.read_excel(r"C:\Users\venki\OneDrive\Documents\working.xlsx")
#df1 = pd.read_excel(r"C:\Users\venki\OneDrive\Documents\Statistics\Statistics3.xlsx")


@app.get("/calculate_percentile/")
async def calculate_percentile(percentile: float):
    # Calculate percentile using Pandas
    percentile_value = df["Income"].quantile(percentile / 100)
    return {"percentile_value": percentile_value}

@app.get("/no_outlier/")
async def no_outlier():
    return session3.no_outliers

@app.get("/outlier/")
async def outlier():
    return session3.outliers




# Example usage: http://localhost:8000/percentiles/salary?percentiles=25,50,75













# from fastapi import FastAPI
# from statistics_internal import session1, session2

# app = FastAPI()


# @app.get("/session1/")
# async def get_data1():
    # return session1.new_data


# @app.get("/session3/")
# async def get_data2():
    # return session2.high_data
