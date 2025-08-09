import React from "react";
import { Link } from "react-router-dom";

export default function LandingPage() {
  return (
    <div className="App">
      <h1>Welcome to InstaGenie</h1>
      <p>Your AI-powered Instagram growth manager.</p>
      <Link to="/onboarding">
        <button>Get Started</button>
      </Link>
    </div>
  );
}