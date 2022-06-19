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
                "fight_url": "http://www.ufcstats.com/fight-details/9a92d376fba2379d",
                "fighter1_name": "Court McGee",
                "fighter2_name": "Jeremiah Wells",
                "winner": "Jeremiah Wells",
                "division": "Welterweight Bout",
                "win_method": "KO/TKO",
                "win_method_details": "Punch to Head At Distance ",
                "referee": "Herb Dean",
                "end_round": 1,
                "end_second": 94,
                "f1_total_knockdown": 0,
                "f1_total_sigstrikes_l": 3,
                "f1_total_sigstrikes_a": 8,
                "f1_total_strikes_l": 3,
                "f1_total_strikes_a": 8,
                "f1_total_takedown_l": 0,
                "f1_total_takedown_a": 0,
                "f1_total_submission_a": 0,
                "f1_total_pass": 0,
                "f1_total_reversal": 0,
                "f2_total_knockdown": 1,
                "f2_total_sigstrikes_l": 7,
                "f2_total_sigstrikes_a": 16,
                "f2_total_strikes_l": 7,
                "f2_total_strikes_a": 16,
                "f2_total_takedown_l": 0,
                "f2_total_takedown_a": 0,
                "f2_total_submission_a": 0,
                "f2_total_pass": 0,
                "f2_total_reversal": 2,
                "event": {
                    "event_name": "UFC Fight Night: Kattar vs. Emmett",
                    "event_date": "2022-06-18T00:00:00",
                    "event_location": "Austin, Texas, USA",
                    "event_url": "http://www.ufcstats.com/event-details/a0a680fe2f6cc8e6",
                },
            }
        }
