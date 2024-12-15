import pandas as pd

data = pd.read_json("../data/academic_network.json")


def get_teachers():
    return data['teachers']


def get_classes():
    return data['classes']


def get_relationships():
    return data['relationships']
