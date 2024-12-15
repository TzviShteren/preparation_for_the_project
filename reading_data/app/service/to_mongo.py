import pandas as pd


def read_data():
    data = pd.read_csv("../data/student_lifestyle.csv")
    return data.to_dict(orient="records")

