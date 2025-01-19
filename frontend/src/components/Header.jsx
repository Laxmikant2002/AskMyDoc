import React from "react";
import "./Header.css";

const Header = () => (
  <header className="header">
    <div className="logo">
      <img src="/path-to-logo.png" alt="Logo" />
      <span>PDF Q&A Assistant</span>
    </div>
    <button className="sign-in-btn">Sign In</button>
  </header>
);

export default Header;