from sqlalchemy import Column, Integer, String, Text
from database import Base

class Users(Base): 
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True, nullable=False)
    email = Column(String(100))
    hashd_password = Column(String, nullable=False)
    description = Column(Text)