from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base
from app.db.models.city_alarm_table import city_alarm


class Alarm(Base):
    __tablename__ = 'alarm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    type_id = Column(Integer, ForeignKey("alerts_type.id"))

    type = relationship("AlertType", back_populates="alarms")
    cities = relationship("City", secondary=city_alarm, back_populates="alarms")
