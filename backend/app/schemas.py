from pydantic import BaseModel

class PDFMetadata(BaseModel):
    id: int
    filename: str
    content: str

    class Config:
        orm_mode = True

class UserQuery(BaseModel):
    id: int
    question: str
    answer: str

    class Config:
        orm_mode = True