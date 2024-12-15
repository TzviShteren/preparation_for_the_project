from kafka_settings.consumer import consume
from dotenv import load_dotenv
from functools import partial
from flask import Flask, render_template, request
import os

load_dotenv(verbose=True)
app = Flask(__name__)


def get_data(data):
    print("Received data:", data)


if __name__ == '__main__':
    partial_consume = partial(
        consume,
        topic=os.environ['GET_NORMALIZED_DATA_TOPIC'],
        function=get_data
    )
    partial_consume()
