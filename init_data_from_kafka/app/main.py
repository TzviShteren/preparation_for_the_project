from kafka_settings.consumer import consume
from dotenv import load_dotenv
from functools import partial
from init_data_from_kafka.app.service.get_the_data import get_student
from flask import Flask, render_template, request
import os

load_dotenv(verbose=True)
app = Flask(__name__)


def get_data(data):
    print("Received data:", data)


if __name__ == '__main__':
    get_student()
