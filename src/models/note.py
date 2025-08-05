from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from models.user import Users

class Notes(Base):
    __tablename__ = "Notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(Text)
    insert_date = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey(Users.id))

    owner = relationship("Users", back_populates="notes_ids")