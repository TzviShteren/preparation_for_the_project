from dotenv import load_dotenv

from reading_data.app.service.data_handlers import (
    process_students,
    process_lifestyle,
    process_performance,
    process_teachers,
    process_classes,
    process_reviews,
    process_relationships
)

load_dotenv(verbose=True)


def main():
    print("Starting batch publishing process...")
    # process_students()
    # process_lifestyle()
    # process_performance()
    # process_teachers()
    # process_classes()
    # process_relationships()
    process_reviews()
    print("Finished publishing all data")


if __name__ == "__main__":
    main()
