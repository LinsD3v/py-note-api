from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from database import Base

class Notes(Base):
    __tablename__ = "Notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(Text)
    insert_date = Column(DateTime, default=datetime.utcnow)
