from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    contacts: List["Contact"] = Relationship(back_populates="owner")


class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: str
    user_id: int = Field(foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="contacts")
