import React from "react";
import "./DocumentList.css";

const DocumentList = ({ documents, onUpload }) => (
  <aside className="sidebar">
    <h3>Documents</h3>
    <ul>
      {documents.map((doc, index) => (
        <li key={index}>
          <i className="pdf-icon" /> {doc.name}
          <i className="options-icon" />
        </li>
      ))}
    </ul>
    <button className="upload-btn" onClick={onUpload}>+</button>
  </aside>
);

export default DocumentList;