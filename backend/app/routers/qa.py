from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..qa_service import process_question
from ..crud import create_user_query
from ..database import SessionLocal

router = APIRouter()

class Question(BaseModel):
    question: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ask")
async def ask_question(question: Question, db: Session = Depends(get_db)):
    if not question.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    answer = process_question(question.question)
    create_user_query(db, question.question, answer)
    return {"answer": answer}