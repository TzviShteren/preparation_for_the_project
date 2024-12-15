from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

elasticsearch_client = Elasticsearch(os.environ['ELASTICSEARCH_URL'], basic_auth=(os.environ['ELASTICSEARCH_USER_NAME'], os.environ['ELASTICSEARCH_PASSWORD']))
