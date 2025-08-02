from fastapi import FastAPI, HTTPException
import os

app = FastAPI()
NOTES_DIR = "notes"

os.makedirs(NOTES_DIR, exist_ok=True)

@app.post("/notes/")
def create_note(title: str, content: str):
    try:
        path = os.path.join(NOTES_DIR, f"{title}.txt")
        if os.path.exists(path):
            raise HTTPException(status_code=400, detail="Note already exists.")
        with open(path, "w") as f:
            f.write(content)
        return {"message": "Note created."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{title}")
def read_note(title: str):
    path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Note not found.")
    with open(path, "r") as f:
        return {"title": title, "content": f.read()}

@app.post("/notes/{title}")
def update_note(title: str, content: str):
    path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Note not found.")
    with open(path, "w") as f:
        f.write(content)
    return {"message": "Note updated."}

@app.delete("/notes/{title}")
def delete_note(title: str):
    path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Note not found.")
    os.remove(path)
    return {"message": "Note deleted."}
