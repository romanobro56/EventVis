import { useEffect, useState } from "react";

export default function Profile() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");
  const API_BASE = "http://localhost:8000";

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        setError("Not logged in");
        return;
      }

      try {
        const res = await fetch(`${API_BASE}/protected`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        const data = await res.json();

        if (!res.ok) {
          setError(data.detail || "Failed to fetch profile");
          return;
        }

        setUser(data);
      } catch (err) {
        console.error(err);
        setError("Network error");
      }
    };

    fetchProfile();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user_name");
    window.location.reload(); // or navigate to login
  };

  if (error) {
    return <p className="text-red-600 mt-4">{error}</p>;
  }

  if (!user) {
    return <p className="mt-4">Loading profile...</p>;
  }

  return (
    <div className="max-w-md mx-auto p-6 border rounded shadow mt-10">
      <h2 className="text-2xl font-bold mb-4 text-green-800">Profile</h2>
      <p>
        <strong>Name:</strong> {user.name}
      </p>
      <p>
        <strong>Email:</strong> {user.email}
      </p>
      <button
        onClick={handleLogout}
        className="mt-4 w-full bg-red-600 text-white py-2 rounded hover:bg-red-700"
      >
        Logout
      </button>
    </div>
  );
}
