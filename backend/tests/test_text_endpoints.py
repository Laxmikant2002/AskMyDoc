from app.main import app
from fastapi.testclient import TestClient
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = TestClient(app)

def test_upload_pdf():
    response = client.post("/pdf/upload/", files={"file": ("test.pdf", b"PDF content here", "application/pdf")})
    assert response.status_code == 200
    assert "text" in response.json()

def test_ask_question():
    response = client.post("/qa/ask", json={"question": "what is the capital of France?"})
    assert response.status_code == 200
    assert "answer" in response.json()

def test_invalid_pdf_upload():
    response = client.post("/pdf/upload/", files={"file": ("test.txt", b"Not a PDF content", "text/plain")})
    assert response.status_code == 400  # Updated to match the error handling

def test_empty_question():
    response = client.post("/qa/ask", json={"question": ""})
    assert response.status_code == 400  # Updated to match the error handling

# Add a simple test to ensure pytest is working
def test_simple():
    assert 1 + 1 == 2