import json
from typing import List

NOTES_FILE = "notes.json"


def load_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_notes(notes: dict):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def add_note(username: str, note: dict):
    notes = load_notes()
    if username not in notes:
        notes[username] = []
    notes[username].append(note)
    save_notes(notes)


def get_notes(username: str) -> List[dict]:
    notes = load_notes()
    return notes.get(username, [])
