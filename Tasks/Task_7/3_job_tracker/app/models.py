from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    applications: List["JobApplication"] = Relationship(back_populates="user")


class JobApplication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company: str
    position: str
    status: str
    date_applied: datetime

    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="applications")
