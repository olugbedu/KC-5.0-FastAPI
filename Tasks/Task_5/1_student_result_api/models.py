from pydantic import BaseModel
from typing import Dict


class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
