from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from .database import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    billing_cycle = Column(String, nullable=False)  # "monthly" | "yearly" | "weekly"
    renewal_date = Column(Date, nullable=False)
    active = Column(Boolean, default=True)
