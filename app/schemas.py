from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int


class NoteOut(NoteBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None

class TaskOut(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        from_attributes = True

class AIQuestion(BaseModel):
    question: str


