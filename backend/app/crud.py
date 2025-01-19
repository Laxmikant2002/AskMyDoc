from sqlalchemy.orm import Session
from .models import PDFMetadata, UserQuery

def create_pdf_metadata(db: Session, filename: str, content: str):
    existing_pdf = db.query(PDFMetadata).filter(PDFMetadata.filename == filename).first()
    if existing_pdf:
        return existing_pdf  # Return existing metadata if exists
    db_pdf_metadata = PDFMetadata(filename=filename, content=content)
    db.add(db_pdf_metadata)
    db.commit()
    db.refresh(db_pdf_metadata)
    return db_pdf_metadata

def create_user_query(db: Session, question: str, answer: str):
    db_user_query = UserQuery(question=question, answer=answer)
    db.add(db_user_query)
    db.commit()
    db.refresh(db_user_query)
    return db_user_query