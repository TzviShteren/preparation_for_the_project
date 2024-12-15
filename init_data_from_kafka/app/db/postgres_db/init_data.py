from app.data.types_alerts_data import alerts
from app.db.models import Base
from app.db.postgres_db import engine
from app.repository.postgres_repository.area_repository import insert_area
from app.repository.postgres_repository.city_repository import insert_city
from app.repository.postgres_repository.type_alert_repository import insert_alert_type
from app.service.filter_cities import get_unique_areas
from app.settings.local_files_config import JSON_CITIES_PATH
from app.utils.json_utils import read_json_data


def init_alert_type_data(type_data):
    ids = [insert_alert_type(alert) for alert in type_data]
    return ids


def init_city_data(city_data):
    ids = [insert_city(city) for city in city_data]
    return ids


def init_area_data(area_data):
    ids = [insert_area(area) for area in area_data]
    return ids


def init_db():
    json_content = read_json_data(JSON_CITIES_PATH)
    Base.metadata.create_all(engine)
    init_alert_type_data(alerts)
    init_area_data(get_unique_areas(json_content))
    init_city_data(json_content)


if __name__ == '__main__':
    pass
    # init_db()
