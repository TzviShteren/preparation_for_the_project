import pandas as pd


def normals_data():
    profiles = pd.read_csv("../data/students-profiles.csv")
    lifestyle = pd.read_csv("../data/student_lifestyle.csv")
    course_performance = pd.read_csv("../data/student_course_performance.csv")

    reviews = pd.read_csv("../data/reviews_with_students.csv")

    academic_network = pd.read_json("../data/academic_network.json")
    teachers = academic_network['teachers']
    classes = academic_network['classes']
    relationships = academic_network['relationships']

