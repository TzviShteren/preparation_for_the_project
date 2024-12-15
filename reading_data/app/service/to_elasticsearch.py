import pandas as pd


def read_data():
    data = pd.read_csv("../data/reviews_with_students.csv")
    return data['student_id', 'content', 'score']
