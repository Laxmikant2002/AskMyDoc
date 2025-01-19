# PDF Q&A Assistant

## Overview

PDF Q&A Assistant is a full-stack application that allows users to upload PDF documents and ask questions regarding the content of these documents. The backend processes these documents and utilizes natural language processing to provide answers to the questions posed by the users.

## Technologies Used

- **Backend**: FastAPI
- **NLP Processing**: LangChain/LLamaIndex
- **Frontend**: React.js
- **Database**: SQLite or PostgreSQL
- **File Storage**: Local filesystem

## Features

- **PDF Upload**: Users can upload PDF documents to the application.
- **Asking Questions**: Users can ask questions related to the content of an uploaded PDF.
- **Displaying Answers**: The application displays the answer to the user’s question.
- **Follow-up Questions**: Users can ask follow-up or new questions on the same document.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm 6+

### Backend Setup

1. **Clone the Repository**:

   ```sh
   git clone <repository-url>
   cd backend
2. **Create and Activate Virtual Environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt

4. **Set Up Environment Variables**:
    Create a .env file in the backend directory with the following content:
    ```sh
    DATABASE_URL=sqlite:///./app.db
    OPENAI_API_KEY=<your-openai-api-key>

5. **Run the Backend Server**:
    ```sh
    uvicorn app.main:app --reload

### Frontend Setup

1. **Navigate to the Frontend Directory**:

    ```sh
    cd ../frontend

2. **Install Dependencies**:

    ```sh
    npm install

3. **Run the Frontend Server**:

    ```sh
    npm start

4. **Access the Application**:

    Open your browser and navigate to http://localhost:3000.

### API Documentation

## Endpoint

1. **Upload PDF**

    URL: /pdf/upload/
    Method: POST
    Request:
        file: PDF file to be uploaded.
    Response:
        200 OK: { "text": "<extracted-text>" }
        400 Bad Request: { "detail": "Error processing the PDF: <error-message>" }

2. **Ask Question**

    URL: /qa/ask
    Method: POST
    Request:
        question: The question to be asked.
    Response:
        200 OK: { "answer": "<answer>" }
        400 Bad Request: { "detail": "Question cannot be empty" }
        429 Too Many Requests: { "detail": "Rate limit exceeded" }
        