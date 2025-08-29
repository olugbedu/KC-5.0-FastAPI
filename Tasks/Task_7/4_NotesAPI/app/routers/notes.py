from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Note
from app.db import get_session
from app.utils import save_notes_to_json

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=Note)
def create_note(note: Note, session: Session = Depends(get_session)):
    session.add(note)
    session.commit()
    session.refresh(note)
    save_notes_to_json(session)
    return note


@router.get("/", response_model=list[Note])
def list_notes(session: Session = Depends(get_session)):
    return session.exec(select(Note)).all()


@router.get("/{note_id}", response_model=Note)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}")
def delete_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    save_notes_to_json(session)
    return {"message": "Note deleted"}
