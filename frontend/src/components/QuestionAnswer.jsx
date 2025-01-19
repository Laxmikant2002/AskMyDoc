import React, { useState } from "react";
import "./QuestionAnswer.css";

const QuestionAnswer = ({ chatHistory, onAsk }) => {
  const [question, setQuestion] = useState("");

  const handleAsk = () => {
    if (question.trim()) {
      onAsk(question);
      setQuestion("");
    }
  };

  return (
    <div className="qa-section">
      <h3>Ask a Question</h3>
      <div className="qa-input">
        <input
          type="text"
          placeholder="Type your question here..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button onClick={handleAsk}>Send</button>
      </div>
      <div className="chat-history">
        {chatHistory.map((chat, index) => (
          <div key={index} className="chat-message">
            <p>{chat.answer}</p>
            <div className="feedback">
              <button>Helpful</button>
              <button>Not helpful</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default QuestionAnswer;