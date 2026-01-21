from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.schemas import NoteCreate, NoteOut
from app.core.jwt import get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_note = models.Note(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


@router.get("/", response_model=list[NoteOut])
def get_my_notes(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    notes = db.query(models.Note).filter(
        models.Note.owner_id == current_user.id
    ).all()

    return notes
