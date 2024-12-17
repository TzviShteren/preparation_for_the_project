# from init_data_from_kafka.app.db.postgres_db.connection import session_maker
from init_data_from_kafka.app.db.elasticsearch_db.connection import elasticsearch_client as ec
from dotenv import load_dotenv
import os
from init_data_from_kafka.app.db.models import StudentProfile
from elasticsearch import Elasticsearch
import uuid
import json

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


def insert_to_elasticsearch(data):
    index_name = "reviews"
    try:
        # Insert the document into Elasticsearch
        res = ec.index(index=index_name, id=data['review_id'], body=data)
        print(f"Inserted review_id: {data['review_id']} -> Result: {res['result']}")
    except Exception as e:
        print(f"Error inserting review_id {data['review_id']}: {e}")
