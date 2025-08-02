from fastapi import FastAPI, HTTPException, Query

app = FastAPI()
contacts = {}

@app.post("/contacts/")
def add_contact(name: str, phone: str, email: str):
    if name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists.")
    contacts[name] = {"phone": phone, "email": email}
    return {"message": "Contact added"}

@app.get("/contacts/")
def get_contact_by_query(name: str = Query(...)):
    contact = contacts.get(name)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return {"name": name, **contact}

@app.post("/contacts/{name}")
def update_contact(name: str, phone: str = "", email: str = ""):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found.")
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    return {"message": "Contact updated"}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found.")
    del contacts[name]
    return {"message": "Contact deleted"}
