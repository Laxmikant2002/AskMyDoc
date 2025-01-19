from sqlalchemy import Column, Integer, String, Text
from .database import Base

class PDFMetadata(Base):
    __tablename__ = "pdf_metadata"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)

class UserQuery(Base):
    __tablename__ = "user_queries"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    answer = Column(Text)