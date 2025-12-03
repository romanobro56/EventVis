import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Signup({ setUser }) {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSignup = async (e) => {
    e.preventDefault();
    setError("");
  
    try {
      const res = await fetch("http://localhost:8000/users/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
  
      const data = await res.json();
  
      if (!res.ok) {
        setError(data.detail || "Signup failed");
        return;
      }
  
      // SAVE TOKEN + USER INFO
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("user_name", data.name);
      localStorage.setItem("user_id", data.user_id);
  
      // UPDATE GLOBAL REACT STATE
      setUser({
        name: data.name,
        user_id: data.user_id,
        token: data.access_token
      });
  
      // REDIRECT TO HOME PAGE
      navigate("/");
    } catch (err) {
      console.error("Signup error:", err);
      setError("Something went wrong. Try again.");
    }
  };
  

  return (
    <div className="max-w-md mx-auto p-8">
      <h2 className="text-3xl font-bold text-green-800 mb-6">Create Account</h2>

      {error && (
        <p className="bg-red-200 text-red-800 p-2 rounded mb-4">{error}</p>
      )}

      <form onSubmit={handleSignup} className="space-y-4">
        <div>
          <label className="block text-gray-700 font-medium">Name</label>
          <input
            type="text"
            className="w-full p-2 border rounded mt-1"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Email</label>
          <input
            type="email"
            className="w-full p-2 border rounded mt-1"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Password</label>
          <input
            type="password"
            className="w-full p-2 border rounded mt-1"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button
          type="submit"
          className="w-full bg-green-700 text-white py-2 rounded hover:bg-green-800"
        >
          Sign Up
        </button>
      </form>

      <div className="mt-6 text-sm text-green-700 font-medium">
        <button onClick={() => navigate("/account")}>Back to Login</button>
      </div>
    </div>
  );
}
