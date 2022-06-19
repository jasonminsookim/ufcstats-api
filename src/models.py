from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "events"
    index = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    event_date = Column(DateTime, index=True)
    event_location = Column(String, index=True)
    event_url = Column(String, index=True)

class Fight(Base):
    __tablename__ = "fights"
    index = Column(Integer, primary_key=True, index=True)
    fighter1_name = Column(String, index=True)
    fighter2_name = Column(String, index=True)
    winner = Column(String, index=True)
    division = Column(String, index=True)
    win_method = Column(String, index=True)
    win_method_details = Column(String, index=True)
    referee = Column(String, index=True)
    end_round = Column(Integer, index=True)
    end_second = Column(Integer, index=True)
    event_url = Column(String, ForeignKey("events.event_url"))
    event = relationship("Event", backref="events")
