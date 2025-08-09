// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyBGlmgBFl_CG1uYyes5TNVJ109zIrNkeI0",
  authDomain: "instagenie-8cf05.firebaseapp.com",
  projectId: "instagenie-8cf05",
  storageBucket: "instagenie-8cf05.firebasestorage.app",
  messagingSenderId: "514873904100",
  appId: "1:514873904100:web:869f8b20f5d12b4e3d15f1",
  measurementId: "G-9X4EFJZLZR"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);

export { db, analytics };
