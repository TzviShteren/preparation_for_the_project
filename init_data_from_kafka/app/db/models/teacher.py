from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from init_data_from_kafka.app.db.models import Base


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    office = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationships
    classes = relationship("Class", back_populates="teacher")
