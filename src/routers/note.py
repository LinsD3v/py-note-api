from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import Sesionlocal
from schemas.note import NoteCreate, NoteOut
from crud.note import create_note as db_create_note, get_note as db_get_note

router = APIRouter()

def get_db():
    db = Sesionlocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def Root():
    return {"message": "OK"}

@router.post("/notes/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)): # aqui o nome estava igual ao importado
    return db_create_note(db, note)

@router.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    return db_get_note(db, note_id)