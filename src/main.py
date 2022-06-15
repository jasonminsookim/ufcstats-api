from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

DESCRIPTION = """
## Data Source / Web Scraping
**Repo:** https://github.com/jasonminsookim/scrape_ufcstats
**Deployed:** Scheduled to run every Monday with Google Cloud Run
**Database:** Heroku Postgres

## UFC Stats API
**Repo:** https://github.com/jasonminsookim/ufcstats-api
"""
app = FastAPI(title="UFC Stats API", description=DESCRIPTION)

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


@app.get("/events", response_model=list[schemas.Event])
async def read_events(skip: int=0, limit: int= 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events


@app.get("/events/{event_id}")
async def read_event(event_id: str):
    return {"event": f"Placeholder event information for {event_id}"}
