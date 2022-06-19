from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Event(BaseModel):
    event_name: str
    event_date: datetime
    event_location: str
    event_url: str

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "event_name": "UFC Fight Night: Kattar vs. Emmett",
                "event_date": "2022-06-18T00:00:00",
                "event_location": "Austin, Texas, USA",
                "event_url": "http://www.ufcstats.com/event-details/a0a680fe2f6cc8e6",
            }
        }



class Fight(BaseModel):
    fight_url: str
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

    # Figher 1: Overall Stats
    f1_total_knockdown: int
    f1_total_sigstrikes_l: int
    f1_total_sigstrikes_a: int
    f1_total_strikes_l: int
    f1_total_strikes_a: int
    f1_total_takedown_l: int
    f1_total_takedown_a: int
    f1_total_submission_a: int
    f1_total_pass: int
    f1_total_reversal: int

    # Fighter 2: Overall Stats
    f2_total_knockdown: int
    f2_total_sigstrikes_l: int
    f2_total_sigstrikes_a: int
    f2_total_strikes_l: int
    f2_total_strikes_a: int
    f2_total_takedown_l: int
    f2_total_takedown_a: int
    f2_total_submission_a: int
    f2_total_pass: int
    f2_total_reversal: int


    event: Event
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "fighter1_name": "Joaquin Buckley",
                "fighter2_name": "Albert Duraev",
                "winner": "Joaquin Buckley",
                "division": "Middleweight Bout",
                "win_method": "TKO - Doctor's Stoppage",
                "win_method_details": " ",
                "referee": "Jacob Montalvo",
                "end_round": 2,
                "end_second": 300,
                "event": {
                    "event_name": "UFC Fight Night: Kattar vs. Emmett",
                    "event_date": "2022-06-18T00:00:00",
                    "event_location": "Austin, Texas, USA",
                    "event_url": "http://www.ufcstats.com/event-details/a0a680fe2f6cc8e6",
                },
            }
        }
