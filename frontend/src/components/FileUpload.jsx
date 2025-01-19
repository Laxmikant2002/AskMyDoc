import React from "react";
import "./FileUpload.css";

const FileUpload = ({ onFileUpload }) => {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.size > 10 * 1024 * 1024) { // 10MB limit
      alert("File size exceeds 10MB!");
      return;
    }
    onFileUpload([file]);
  };

  return (
    <div className="upload-area">
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <i className="upload-icon fas fa-upload" />
      <p>Drop your PDF here or browse</p>
      <p className="size-limit">PDF up to 10MB</p>
    </div>
  );
};

export default FileUpload;