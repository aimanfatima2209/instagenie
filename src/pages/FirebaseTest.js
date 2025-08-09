// src/pages/FirebaseTest.js
import React, { useEffect, useState } from "react";
import { db } from "../firebase";
import { collection, getDocs } from "firebase/firestore";

export default function FirebaseTest() {
  const [status, setStatus] = useState("Testing connection...");

  useEffect(() => {
    const testConnection = async () => {
      try {
        const querySnapshot = await getDocs(collection(db, "testCollection"));
        let data = [];
        querySnapshot.forEach((doc) => {
          data.push({ id: doc.id, ...doc.data() });
        });

        if (data.length > 0) {
          setStatus(`✅ Firestore connected! Found ${data.length} document(s).`);
          console.log("Documents:", data);
        } else {
          setStatus("⚠ Connected but no data found in 'testCollection'.");
        }
      } catch (error) {
        setStatus("❌ Connection failed. Check console for error.");
        console.error("Firestore connection error:", error);
      }
    };

    testConnection();
  }, []);

  return (
  <div className="App">
    <header className="App-header">
      <h1>Firebase Connection Test</h1>
    </header>
    <p>{status}</p>
  </div>
);
}
