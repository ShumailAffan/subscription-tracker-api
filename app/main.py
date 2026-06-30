from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Subscription Tracker API",
    description="REST API for tracking recurring subscriptions, renewal dates, and spend categories.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Subscription Tracker API is running. Visit /docs for the interactive API explorer."}


@app.post("/subscriptions", response_model=schemas.Subscription, status_code=201)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.create_subscription(db, subscription)


@app.get("/subscriptions", response_model=list[schemas.Subscription])
def list_subscriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_subscriptions(db, skip=skip, limit=limit)


@app.get("/subscriptions/upcoming-renewals", response_model=list[schemas.Subscription])
def upcoming_renewals(days: int = Query(7, ge=1, le=365), db: Session = Depends(get_db)):
    """Return active subscriptions renewing within the next N days (default 7)."""
    return crud.get_upcoming_renewals(db, days=days)


@app.get("/subscriptions/{subscription_id}", response_model=schemas.Subscription)
def get_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_sub = crud.get_subscription(db, subscription_id)
    if db_sub is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_sub


@app.put("/subscriptions/{subscription_id}", response_model=schemas.Subscription)
def update_subscription(subscription_id: int, subscription: schemas.SubscriptionUpdate, db: Session = Depends(get_db)):
    db_sub = crud.update_subscription(db, subscription_id, subscription)
    if db_sub is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_sub


@app.delete("/subscriptions/{subscription_id}", status_code=204)
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_sub = crud.delete_subscription(db, subscription_id)
    if db_sub is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return None
