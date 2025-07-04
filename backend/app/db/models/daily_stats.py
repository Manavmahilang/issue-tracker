from sqlalchemy import Column, Date, Integer
from app.db.base import Base

class DailyStats(Base):
    __tablename__ = "daily_stats"

    date = Column(Date, primary_key=True)
    created_issues = Column(Integer, default=0)
    resolved_issues = Column(Integer, default=0)
