from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import desc


def get_events(
    db: Session, skip: int = 0, limit: int = 100, date_descending: bool = True
):
    if date_descending:
        return (
            db.query(models.Event)
            .order_by(desc(models.Event.event_date))
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        return (
            db.query(models.Event)
            .order_by(models.Event.event_date)
            .offset(skip)
            .limit(limit)
            .all()
        )


def get_event_by_name(db: Session, event_name: str):
    return db.query(models.Event).filter(models.Event.event_name == event_name).first()


def get_fights(
    db: Session, skip: int = 0, limit: int = 100, date_descending: bool = True
):
    return db.query(models.Fight).offset(skip).limit(limit).all()
