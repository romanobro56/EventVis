import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Account({ setUser }) {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const API_BASE = "http://localhost:8000"; // change if your backend runs elsewhere

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
  
    try {
      const res = await fetch("http://localhost:8000/users/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
  
      const data = await res.json();
  
      if (!res.ok) {
        setError(data.detail || "Something went wrong");
        return;
      }
  
      localStorage.setItem("token", data.access_token);
      localStorage.setItem("user_name", data.name);
      localStorage.setItem("user_id", data.user_id);
  
      setUser({
        name: data.name,
        user_id: data.user_id,
        token: data.access_token
      });
  
      navigate("/");   // ← ALWAYS go home
    } catch (err) {
      console.error(err);
      setError("Network error");
    }
  };
  

  return (
    <div className="max-w-md mx-auto p-6 border rounded shadow mt-10">
      <h2 className="text-2xl font-bold mb-4 text-green-800">Login</h2>

      {error && <p className="text-red-600 mb-2">{error}</p>}

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />

        <button
          type="submit"
          className="w-full bg-green-700 text-white py-2 rounded hover:bg-green-800"
        >
          Login
        </button>
      </form>

      <p className="mt-4 text-center text-gray-600">
        Don&apos;t have an account?{" "}
        <button
          className="text-green-700 font-semibold"
          onClick={() => navigate("/signup")}
        >
          Sign Up
        </button>
      </p>
    </div>
  );
}
