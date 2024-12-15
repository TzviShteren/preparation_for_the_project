from sqlalchemy.orm import declarative_base

from init_data_from_kafka.app.db.postgres_db.connection import engine

Base = declarative_base()

from .student_profile_model import StudentProfile
from .student_course_performance_model import StudentCoursePerformance
from .student_lifestyle_model import StudentLifestyle
