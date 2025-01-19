from fastapi import FastAPI
from .routers import pdf, qa
from .database import engine
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
app.include_router(qa.router, prefix="/qa", tags=["qa"])