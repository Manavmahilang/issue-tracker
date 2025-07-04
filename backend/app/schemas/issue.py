from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Status(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"

class IssueCreate(BaseModel):
    title: str
    description: str
    severity: Severity

class IssueOut(IssueCreate):
    id: int
    status: Status
    created_at: datetime

    class Config:
        orm_mode = True
