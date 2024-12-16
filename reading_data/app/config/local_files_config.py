from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent

load_dotenv(verbose=True)

STUDENTS_PROFILES = PROJECT_ROOT / 'data' / 'students-profiles.csv'
STUDENT_LIFESTYLE = PROJECT_ROOT / 'data' / 'student_lifestyle.csv'
STUDENT_PERFORMANCE = PROJECT_ROOT / 'data' / 'student_course_performance.csv'
REVIEWS_WITH_STUDENTS = PROJECT_ROOT / 'data' / 'reviews_with_students.csv'
ACADEMIC_NETWORK = PROJECT_ROOT / 'data' / 'academic_network.json'

