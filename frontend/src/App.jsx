import React, { useState } from 'react';
import Header from './components/Header';
import DocumentList from './components/DocumentList';
import FileUpload from './components/FileUpload';
import QuestionAnswer from './components/QuestionAnswer';
import './App.css';
import axios from 'axios';

function App() {
    const [documents, setDocuments] = useState([]);
    const [chatHistory, setChatHistory] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileUpload = async (uploadedFiles) => {
        const formData = new FormData();
        formData.append('file', uploadedFiles[0]);

        setLoading(true);
        setError(null);

        try {
            const response = await axios.post('http://localhost:8000/pdf/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            const newDocument = {
                id: documents.length + 1,
                name: uploadedFiles[0].name,
                text: response.data.text,
            };
            setDocuments([...documents, newDocument]);
        } catch (error) {
            console.error('Error uploading file:', error);
            setError('Failed to upload file. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const handleAskQuestion = async (question) => {
        setLoading(true);
        setError(null);

        try {
            const response = await axios.post('http://localhost:8000/qa/ask', { question });
            const answer = response.data.answer;
            setChatHistory([...chatHistory, { question, answer }]);
        } catch (error) {
            console.error('Error asking question:', error);
            if (error.response && error.response.data.detail === "Rate limit exceeded") {
                setError('Rate limit exceeded. Please try again later.');
            } else {
                setError('Failed to get an answer. Please try again later.');
            }
        } finally {
            setLoading(false);
        }
    };

    const handleClearChat = () => setChatHistory([]);

    return (
        <div className="App">
            <Header />
            <div className="container">
                <DocumentList documents={documents} onUpload={() => document.querySelector('.upload-area input').click()} />
                <div className="main-content">
                    <FileUpload onFileUpload={handleFileUpload} />
                    <QuestionAnswer onAsk={handleAskQuestion} chatHistory={chatHistory} />
                    {loading && <p>Loading...</p>}
                    {error && <p className="error">{error}</p>}
                </div>
            </div>
            <footer className="footer">
                <button onClick={handleClearChat}>Clear Chat</button>
                <button>Download History</button>
                <div className="connection-status">
                    <span className="dot"></span> Connected
                </div>
            </footer>
        </div>
    );
}

export default App;