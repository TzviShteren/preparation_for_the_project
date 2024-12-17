# from init_data_from_kafka.app.db.postgres_db.connection import session_maker
from init_data_from_kafka.app.db.elasticsearch_db.connection import elasticsearch_client as es
from dotenv import load_dotenv
import os
from init_data_from_kafka.app.db.models import StudentProfile
from elasticsearch import Elasticsearch
import pandas as pd
load_dotenv(verbose=True)


# def student_to_psql(data):
#     with session_maker() as session:
#         try:
#             new_student = StudentProfile(
#
#                 first_name=data["value"],
#                 last_name=data["name"],
#                 age=data["name_en"],
#                 address=data["name_ru"],
#             )
#             session.add(new_student)
#             session.commit()
#             session.refresh(new_student)
#             print(data)
#             return new_student.id
#         except Exception as e:
#             session.rollback()
#             print(f"Error occurred: {e}")


def insert_to_elasticsearch(data: dict):
    index_name = "reviews"
    cleaned_data = {k: (v if v is not None else 'N/A') for k, v in data.items()}
    try:
        res = es.index(index=index_name, id=cleaned_data['review_id'], body=cleaned_data)
        print(f"Inserted review_id: {cleaned_data['review_id']} -> Result: {res['result']}")
    except Exception as e:
        print(f"Error inserting review_id {cleaned_data['review_id']}: {e}")


def delete_all_reviews():
    index_name = "reviews"
    try:
        response = es.delete_by_query(
            index=index_name,
            body={"query": {"match_all": {}}},
            conflicts="proceed"
        )
        print(f"Deleted {response['deleted']} documents from index '{index_name}'")
    except Exception as e:
        print(f"Error deleting documents: {e}")

