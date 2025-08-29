from sqlmodel import SQLModel, Field
from typing import Optional, List


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str
    grades: str  # store grades as JSON string or comma-separated values
