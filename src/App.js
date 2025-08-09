// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import Onboarding from "./pages/Onboarding";
import Dashboard from "./pages/Dashboard";
import Insights from "./pages/Insights";
import FirebaseTest from "./pages/FirebaseTest"; // ⬅ add this
import "./styles/style.css";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/onboarding" element={<Onboarding />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/insights" element={<Insights />} />
        <Route path="/firebase-test" element={<FirebaseTest />} /> {/* temp test route */}
      </Routes>
    </Router>
  );
}

export default App;