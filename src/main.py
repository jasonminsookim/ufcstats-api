from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

DESCRIPTION = """
## Data Source / Web Scraping
- **Repo:** https://github.com/jasonminsookim/scrape_ufcstats
- **Deployed:** Scheduled to run every Monday with Google Cloud Run
- **Database:** Heroku Postgres

## UFC Stats API
- **Repo:** https://github.com/jasonminsookim/ufcstats-api
"""

TAGS_METADATA = [
    {"name": "events", "description": "The metadata related to UFC events."},
    {
        "name": "fights",
        "description": "Fighter details, referee metadata, and stoppage metadata.",
    },
]

app = FastAPI(
    title="UFC Stats API", description=DESCRIPTION, openapi_tags=TAGS_METADATA
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/events/", response_model=list[schemas.Event], tags=["events"])
async def read_events(
    skip: int = 0,
    limit: int = 100,
    date_descending: bool = True,
    db: Session = Depends(get_db),
):
    events = crud.get_events(
        db, skip=skip, limit=limit, date_descending=date_descending
    )
    return events


@app.get("/events/{event_name}", response_model=schemas.Event, tags=["events"])
async def get_event_by_name(event_name: str, db: Session = Depends(get_db)):
    event = crud.get_event_by_name(db, event_name)
    return event


@app.get("/fights/", response_model=list[schemas.Fight], tags=["fights"])
async def read_fights(
    skip: int = 0,
    limit: int = 100,
    date_descending: bool = True,
    db: Session = Depends(get_db),
):
    fights = crud.get_fights(
        db,
        skip=skip,
        limit=limit,
        date_descending=date_descending,
    )
    return fights
