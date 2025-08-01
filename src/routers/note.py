from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from database import Sesionlocal
from schemas.note import NoteCreate, NoteOut, NoteUpdate
from typing import List, Optional
from models.note import Notes
from crud.note import create_note as db_create_note, get_all_notes as db_get_notes, get_note as db_get_note, update_note as db_update_note

router = APIRouter()

def get_db():
    db = Sesionlocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/notes/", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    return db_create_note(db, note)


@router.get("/notes/", response_model=List[NoteOut])
def get_notes(busca: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if busca:
        return db.query(Notes).filter(Notes.title.ilike(f"%{busca}%")).all()
    return db.query(Notes).all()

    
@router.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
        return db_get_note(db, note_id)
        

@router.put("/notes/{note_id}", response_model=NoteOut)
def put_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    updated = db_update_note(db, note_id, note)
    if not updated: 
         raise HTTPException(status_code=404, detail="Nota não encontrada")
    return updated