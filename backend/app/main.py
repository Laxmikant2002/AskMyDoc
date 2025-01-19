from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import pdf, qa
from .database import engine
from .models import Base

app = FastAPI()

# Allow CORS for all origins (you can restrict this to specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
app.include_router(qa.router, prefix="/qa", tags=["qa"])