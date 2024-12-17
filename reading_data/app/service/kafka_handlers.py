from typing import List, Dict, Any

from kafka_settings.producer import produce


def publish_batch(topic: str, batch: List[Dict[str, Any]], id_field: str):
    try:
        for record in batch:
            produce(
                topic=topic,
                key=str(record[id_field]) if record[id_field] else None,
                value=record
            )
        print(f"Published batch of {len(batch)} records to {topic}")
    except Exception as e:
        print(f"Error publishing batch to {topic}: {str(e)}")