from pydantic import BaseModel
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    email: str
    hashd_password: str
    description: Optional[str]
    
class UserOut(BaseModel):
    id: int
    username: str
    email: str
    hashd_password: str
    description: Optional[str]
    notes: List[int]
    
    class Config:
        orm_mode: True
        
