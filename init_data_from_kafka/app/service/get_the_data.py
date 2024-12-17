from init_data_from_kafka.app.repository.init_data import insert_to_elasticsearch
from kafka_settings.consumer import consume
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def get_student():
    print(1)
    consume(
        topic=os.environ['RAW_REVIEWS'],
        function=insert_to_elasticsearch,
    )

