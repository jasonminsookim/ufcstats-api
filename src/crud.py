from sqlalchemy.orm import Session
import models, schemas


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()
