from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    event_name: str
    event_date: datetime
    event_location: str
    event_url: str
    datetime_scraped: datetime

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "event_name": "UFC 275: Teixeira vs. Prochazka",
                "event_date": "2022-06-11T00:00:00",
                "event_location": "Kallang, Singapore",
                "event_url": "http://www.ufcstats.com/event-details/3a24769a4855040a",
                "datetime_scraped": "2022-06-15T00:22:08.534576"
            }
        }