from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    event_url: str
    datetime_scraped: datetime

    class Config:
        orm_mode = True
