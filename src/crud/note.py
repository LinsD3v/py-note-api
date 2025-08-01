from sqlalchemy.orm import Session
from models.note import Notes
from schemas.note import NoteCreate, NoteUpdate

def create_note(db:Session, note: NoteCreate):
    db_note = Notes(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_all_notes(db: Session):
    return db.query(Notes).all()

def get_note(db: Session, note_id: int):
    return db.query(Notes).filter(Notes.id == note_id).first()

def update_note(db: Session, note_id: int, note_data: NoteUpdate):
    note = db.query(Notes). filter(Notes.id == note_id).first()
    if not note:
        return None
    if note_data.title is not None:
        note.title = note_data.title
    if note_data.content is not None:
        note.content = note_data.content

    db.commit()
    db.refresh(note)
    return note
