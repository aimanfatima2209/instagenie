import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Insights() {
  const [insights, setInsights] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/get-insights")
      .then(res => setInsights(res.data))
      .catch(err => console.error(err));
  }, []);

 return (
  <div className="App">
    <header className="App-header">
      <h2>Profile Insights</h2>
    </header>
    {insights ? (
      <pre>{JSON.stringify(insights, null, 2)}</pre>
    ) : (
      "Loading..."
    )}
  </div>
);
}
