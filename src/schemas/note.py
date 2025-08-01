from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    title: str
    content: str
    
class NoteOut(BaseModel):
    id: int 
    title: str
    content: str
    insert_date: datetime

    class Config:
        orm_mode: True


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None