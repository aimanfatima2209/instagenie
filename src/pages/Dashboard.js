import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [caption, setCaption] = useState("");

  useEffect(() => {
    axios.post("http://localhost:8000/generate-caption", {
      niche: "Travel",
      tone: "Aesthetic"
    })
    .then(res => setCaption(res.data.caption))
    .catch(err => console.error(err));
  }, []);

  return (
  <div className="App">
    <header className="App-header">
      <h2>Your AI Caption</h2>
    </header>
    <p>{caption || "Loading..."}</p>
  </div>
);
}
