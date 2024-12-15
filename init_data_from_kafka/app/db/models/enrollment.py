from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from init_data_from_kafka.app.db.models import Base


class Enrollment(Base):
    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student_profile.id'))
    class_id = Column(String, ForeignKey('class.id'))
    teacher_id = Column(String, ForeignKey('teacher.id'))
    enrollment_date = Column(Date, nullable=False)
    relationship_type = Column(String, nullable=False)

    # Relationships
    student = relationship("StudentProfile", back_populates="enrollments")
    class_ = relationship("Class", back_populates="enrollments")
    teacher = relationship("Teacher")
