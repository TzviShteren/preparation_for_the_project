from dotenv import load_dotenv
from kafka_settings.producer import produce
from flask import jsonify, Flask
import pandas as pd
import os

load_dotenv(verbose=True)
app = Flask(__name__)


def read_data():
    data = pd.read_csv("data/student_lifestyle.csv")
    return data.to_json(orient="records")


@app.route('/', methods=['POST'])
def all_messages():
    try:
        data = read_data()

        if not data:
            return jsonify({"error": "No data"}), 400

        produce(
            os.environ['GET_NORMALIZED_DATA_TOPIC'],
            key='Student',
            value=data
        )

        # data.produce_member(data)
        return jsonify({"message": "Data send successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)