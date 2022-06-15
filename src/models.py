from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "events"
    event_name = Column(String, index=True)
    event_date = Column(DateTime, index=True)
    event_location = Column(String, index=True)
    event_url = Column(String, index=True, primary_key=True)
    datetime_scraped = Column(DateTime, index=True)

