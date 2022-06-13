from pydantic import BaseModel

class Event(BaseModel):
    event_url: str
    datetime_scraped: str

    class Config:
        orm_mode = True
