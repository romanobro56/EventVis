import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { requestSignUp } from "../api";

export default function Signup({ setUser }) {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    setError("");
  
    try {
      const res = await requestSignUp(formData.name, formData.email, formData.password);
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
            name="name"
            className="w-full p-2 border rounded mt-1"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Email</label>
          <input
            type="email"
            name="email"
            className="w-full p-2 border rounded mt-1"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Password</label>
          <input
            type="password"
            name="password"
            className="w-full p-2 border rounded mt-1"
            value={formData.password}
            onChange={handleChange}
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
