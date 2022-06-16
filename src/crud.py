from sqlalchemy.orm import Session
import models, schemas


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def get_event_by_name(db: Session, event_name: str):
    return db.query(models.Event).filter(models.Event.event_name == event_name).first()

#def get_event()