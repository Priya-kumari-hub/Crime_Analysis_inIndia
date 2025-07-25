from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_women = pd.read_csv("../df_women.csv")
df1 = pd.read_csv("../df1.csv")
df2 = pd.read_csv("../df2.csv")


@app.get("/")
def root():
    return {"message": "Crime Analysis API is running!"}

@app.get("/women-crime/{state}")
def women_crime(state: str):
    row = df_women[df_women["States"].str.lower() == state.lower()]
    if row.empty:
        return {"error": "State not found"}
    return row.to_dict(orient="records")[0]

@app.get("/gender-victims/{state}")
def gender_victims(state: str):
    row = df2[df2["States"].str.lower() == state.lower()]
    if row.empty:
        return {"error": "State not found"}
    return row.to_dict(orient="records")[0]

@app.get("/year-trend/{state}")
def year_trend(state: str):
    row = df1[df1["States"].str.lower() == state.lower()]
    if row.empty:
        return {"error": "State not found"}
    return row[["2020", "2021", "2022"]].to_dict(orient="records")[0]
