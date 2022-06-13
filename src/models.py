from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "events"
    event_url = Column(String, index=True, primary_key=True)
    datetime_scraped = Column(String, index=True)


