import json
from pymongo import ReplaceOne
from typing import List, Dict, Any

from app.db.mongo_db.connection import get_city_alert_details_collection
from app.settings.local_files_config import JSON_CITIES_PATH
from app.utils.json_utils import read_json_data


def import_locations_to_mongodb(locations: List[Dict[str, Any]], collection=None) -> None:
    if collection is None:
        from app.db.mongo_db.connection import get_city_alert_details_collection
        collection = get_city_alert_details_collection()

    collection.create_index("value", unique=True)

    operations = [
        ReplaceOne(
            filter={'value': location['value']},
            replacement=location,
            upsert=True
        )
        for location in locations
    ]

    try:
        result = collection.bulk_write(operations)
        print(f"""
            Successfully processed {len(locations)} locations:
            - Modified: {result.modified_count}
            - Upserted: {result.upserted_count}
        """)
    except Exception as e:
        print(f"Error during bulk import: {e}")
        raise


def load_locations_to_db(json_content: str, collection=None) -> None:
    try:
        locations = read_json_data(json_content)
        import_locations_to_mongodb(locations, collection)
    except json.JSONDecodeError as e:
        print(f"Import failed: {e}")
        raise
    except Exception as e:
        print(f"Import failed: {e}")


if __name__ == '__main__':
    load_locations_to_db(JSON_CITIES_PATH, get_city_alert_details_collection())
