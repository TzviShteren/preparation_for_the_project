import os
from functools import partial
from typing import Dict, Any, Callable, List, Generator
from reading_data.app.service.kafka_handlers import publish_batch
from reading_data.app.utils.file_handlers_repo import read_csv_file, read_json_file
from dotenv import load_dotenv
import pandas as pd

from reading_data.app.config.local_files_config import (
    STUDENTS_PROFILES,
    STUDENT_LIFESTYLE,
    STUDENT_PERFORMANCE,
    REVIEWS_WITH_STUDENTS,
    ACADEMIC_NETWORK
)

load_dotenv(verbose=True)


def create_batches(data: List[Dict[str, Any]], batch_size: int = 5) -> Generator[List[Dict[str, Any]], None, None]:
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def process_csv_data(
        file_path: str,
        topic: str,
        id_field: str,
        transform_func: Callable[[Dict[str, Any]], Dict[str, Any]] = lambda x: x
):
    df = read_csv_file(file_path)
    data = df.to_dict('records')

    for batch in create_batches(data):
        transformed_batch = [transform_func(record) for record in batch]
        publish_batch(topic, transformed_batch, id_field)


def process_json_data(
        file_path: str,
        topic: str,
        id_field: str,
        data_type: str,
        json_path: str
):
    data = read_json_file(file_path)
    records = data[json_path]

    for batch in create_batches(records):
        transformed_batch = [{'type': data_type, 'data': record} for record in batch]
        publish_batch(topic, transformed_batch, id_field)


process_students = partial(
    process_csv_data,
    file_path=STUDENTS_PROFILES,
    topic=os.environ['RAW_STUDENTS'],
    id_field='id'
)

process_lifestyle = partial(
    process_csv_data,
    file_path=STUDENT_LIFESTYLE,
    topic=os.environ['RAW_LIFESTYLE'],
    id_field='Student_ID'
)

process_performance = partial(
    process_csv_data,
    file_path=STUDENT_PERFORMANCE,
    topic=os.environ['RAW_PERFORMANCE'],
    id_field='student_id'
)

process_reviews = partial(
    process_csv_data,
    file_path=REVIEWS_WITH_STUDENTS,
    topic=os.environ['RAW_REVIEWS'],
    id_field='review_id'
)

process_teachers = partial(
    process_json_data,
    file_path=ACADEMIC_NETWORK,
    topic=os.environ['RAW_ACADEMIC'],
    id_field='id',
    data_type='teacher',
    json_path='teachers'
)

process_classes = partial(
    process_json_data,
    file_path=ACADEMIC_NETWORK,
    topic=os.environ['RAW_ACADEMIC'],
    id_field='id',
    data_type='class',
    json_path='classes'
)

process_relationships = partial(
    process_json_data,
    file_path=ACADEMIC_NETWORK,
    topic=os.environ['RAW_ACADEMIC'],
    id_field='student_id',
    data_type='relationship',
    json_path='relationships'
)
