from datetime import date, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas


def get_subscription(db: Session, subscription_id: int):
    return db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()


def get_subscriptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subscription).offset(skip).limit(limit).all()


def create_subscription(db: Session, subscription: schemas.SubscriptionCreate):
    db_sub = models.Subscription(**subscription.model_dump())
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub


def update_subscription(db: Session, subscription_id: int, subscription: schemas.SubscriptionUpdate):
    db_sub = get_subscription(db, subscription_id)
    if not db_sub:
        return None
    update_data = subscription.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_sub, key, value)
    db.commit()
    db.refresh(db_sub)
    return db_sub


def delete_subscription(db: Session, subscription_id: int):
    db_sub = get_subscription(db, subscription_id)
    if not db_sub:
        return None
    db.delete(db_sub)
    db.commit()
    return db_sub


def get_upcoming_renewals(db: Session, days: int = 7):
    today = date.today()
    cutoff = today + timedelta(days=days)
    return (
        db.query(models.Subscription)
        .filter(
            and_(
                models.Subscription.renewal_date >= today,
                models.Subscription.renewal_date <= cutoff,
                models.Subscription.active == True,  # noqa: E712
            )
        )
        .order_by(models.Subscription.renewal_date)
        .all()
    )
