from sqlalchemy import Column, Integer, String,Float, ForeignKey
from database import Base


class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True,index=True)
    value = Column(Float)
    unit = Column(String)
    device_id = Column(Integer, ForeignKey("devices.id"))
