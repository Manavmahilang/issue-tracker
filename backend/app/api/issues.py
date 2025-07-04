from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.utils import get_current_user, get_db
from app.schemas.issue import IssueCreate, IssueOut
from app.db.models.issues import Issue


router = APIRouter()

@router.get("/", response_model=list[IssueOut])
def list_issues(db: Session = Depends(get_db)):
    return db.query(Issue).all()

@router.post("/", response_model=IssueOut)
def create_issue(data: IssueCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    issue = Issue(**data.dict(), reporter_id=user.id)
    db.add(issue)
    db.commit()
    db.refresh(issue)
    return issue
