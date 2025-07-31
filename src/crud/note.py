from sqlalchemy.orm import Session
from models.note import Notes
from schemas.note import NoteCreate

def create_note(db:Session, note: NoteCreate):
    db_note = Notes(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note(db: Session, note_id: int):
    return db.query(Notes).filter(Notes.id == note_id).first()