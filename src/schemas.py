from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


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
                "datetime_scraped": "2022-06-15T00:22:08.534576",
            }
        }


class Fight(BaseModel):
    fighter1_name: str
    fighter2_name: str
    winner: str
    division: str
    win_method: str
    win_method_details: Optional[str] = Field(None)
    referee: Optional[str] = Field(None)
    end_round: Optional[int] = Field(
        None, description="The round number the fight ended in."
    )
    end_second: Optional[int] = Field(
        None,
        description="The number of seconds into the round, in which the fight ended.",
    )
    fight_url: str
    event_url: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "fighter1_name": "Alexander Volkanovski",
                "fighter2_name": "Chan Sung Jung",
                "winner": "Alexander Volkanovski",
                "division": "UFC Featherweight Title Bout",
                "win_method": "KO/TKO",
                "win_method_details": "Punches to Head At Distance ",
                "referee": "Herb Dean",
                "end_round": 4,
                "end_second": 45,
                "fight_url": "http://www.ufcstats.com/fight-details/dc0ab34f1952cb48",
                "event_url": "http://www.ufcstats.com/event-details/3a97fda0de6f1fa4",
            }
        }
