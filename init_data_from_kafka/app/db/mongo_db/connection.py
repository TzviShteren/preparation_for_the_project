from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def get_mongo_client():
    return MongoClient(os.environ['MONGO_URL'])


def get_city_alert_details_collection():
    db = get_mongo_client()['students']
    return db['reviews']


def get_real_time_alarm_collection():
    db = get_mongo_client()['students']
    return db['real_time_alarm']
