import json
from app.models import Note
from sqlmodel import Session, select


def save_notes_to_json(session: Session):
    notes = session.exec(select(Note)).all()
    with open("notes.json", "w") as f:
        json.dump([note.dict() for note in notes], f, indent=4, default=str)
