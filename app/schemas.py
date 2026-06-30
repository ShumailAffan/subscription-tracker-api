from datetime import date
from pydantic import BaseModel, ConfigDict


class SubscriptionBase(BaseModel):
    name: str
    category: str
    cost: float
    billing_cycle: str
    renewal_date: date
    active: bool = True


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    cost: float | None = None
    billing_cycle: str | None = None
    renewal_date: date | None = None
    active: bool | None = None


class Subscription(SubscriptionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
