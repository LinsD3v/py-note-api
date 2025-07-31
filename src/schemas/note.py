from pydantic import BaseModel
from datetime import datetime

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
