from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from init_data_from_kafka.app.db.models import Base


class StudentProfile(Base):
    __tablename__ = 'student_profile'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    # Relationships
    course_performance = relationship("StudentCoursePerformance", back_populates="student")
    lifestyle = relationship("StudentLifestyle", back_populates="student")
