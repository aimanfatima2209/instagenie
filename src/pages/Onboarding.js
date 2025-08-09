import React, { useState } from "react";
import { db } from "../firebase";
import { collection, addDoc } from "firebase/firestore";

export default function Onboarding() {
  const [niche, setNiche] = useState("");
  const [tone, setTone] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addDoc(collection(db, "users"), {
        niche,
        tone,
        createdAt: new Date()
      });
      alert("Preferences saved!");
    } catch (error) {
      console.error("Error saving data: ", error);
    }
  };

  return (
    <div className="App">
      <h2>Select Your Preferences</h2>
      <form onSubmit={handleSubmit}>
        <label>Niche: </label>
        <select value={niche} onChange={(e) => setNiche(e.target.value)} required>
          <option value="">Select...</option>
          <option value="Travel">Travel</option>
          <option value="Fashion">Fashion</option>
          <option value="Food">Food</option>
          <option value="Fitness">Fitness</option>
          <option value="Tech">Tech</option>
        </select>

        <br /><br />

        <label>Tone: </label>
        <select value={tone} onChange={(e) => setTone(e.target.value)} required>
          <option value="">Select...</option>
          <option value="Funny">Funny</option>
          <option value="Aesthetic">Aesthetic</option>
          <option value="Emotional">Emotional</option>
        </select>

        <br /><br />

        <button type="submit">Save</button>
      </form>
    </div>
  );
}