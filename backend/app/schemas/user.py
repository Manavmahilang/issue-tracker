from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    MAINTAINER = "MAINTAINER"
    REPORTER = "REPORTER"

class UserOut(BaseModel):
    id: int
    email: str
    role: RoleEnum

    class Config:
        orm_mode = True
