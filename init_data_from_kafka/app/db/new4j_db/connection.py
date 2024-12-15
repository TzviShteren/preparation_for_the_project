from dotenv import load_dotenv
from neo4j import GraphDatabase
import os

load_dotenv(verbose=True)

neo4j_driver = GraphDatabase.driver(
    os.environ['NEO4J_URL'],
    auth=(os.environ['NEO4J_USERNAME'], os.environ['NEO4J_PASSWORD']),
)
