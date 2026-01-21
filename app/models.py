from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    notes = relationship("Note", back_populates="owner")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="notes")
