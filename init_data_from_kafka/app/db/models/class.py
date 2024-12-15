from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from init_data_from_kafka.app.db.models import Base


class Class(Base):
    __tablename__ = 'class'

    id = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    section = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    room = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    teacher_id = Column(String, ForeignKey('teacher.id'))

    # Relationships
    teacher = relationship("Teacher", back_populates="classes")
    enrollments = relationship("Enrollment", back_populates="class_")
