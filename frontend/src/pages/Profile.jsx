import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const [user, setUser] = useState(null);
  const [savedEvents, setSavedEvents] = useState([]);
  const [createdEvents, setCreatedEvents] = useState([]); // future use
  const [error, setError] = useState("");

  const API = "http://localhost:8000";
  const navigate = useNavigate();

  // ---------------- FETCH PROFILE + SAVED EVENTS ----------------
  useEffect(() => {
    const loadProfile = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        setError("Not Logged In");
        return;
      }

      try {
        // GET user info
        const userRes = await fetch(`${API}/users/protected`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        const userData = await userRes.json();
        if (!userRes.ok) {
          setError(userData.detail || "Failed to load user");
          return;
        }
        setUser(userData);

        // GET saved events
        const savedRes = await fetch(`${API}/users/saved`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        const savedData = await savedRes.json();
        if (savedRes.ok) {
          setSavedEvents(savedData.saved_events || []);
        }
      } catch (err) {
        console.error(err);
        setError("Network error");
      }
    };

    loadProfile();
  }, []);

  // ---------------- UNSAVE EVENT ----------------
  const unsaveEvent = async (eventId) => {
    const token = localStorage.getItem("token");
    if (!token) return;

    await fetch(`${API}/events/${eventId}/unsave`, {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });

    // Update UI
    setSavedEvents((prev) => prev.filter((e) => e._id !== eventId));
  };

  // ---------------- RENDERING ----------------
  if (error) {
    return (
      <div className="max-w-4xl mx-auto mt-16 text-left text-red-600 text-lg">
        {error}
      </div>
    );
  }

  if (!user) {
    return (
      <div className="max-w-4xl mx-auto mt-16 text-left text-gray-600">
        Loading profile...
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto mt-12 px-6 flex flex-col gap-12">

      {/* ================= USER INFO ================= */}
      <div>
        <h1 className="text-4xl font-bold text-green-800">{user.name}</h1>
        <p className="text-lg text-gray-700 mt-1">{user.email}</p>
      </div>

      {/* ================= SAVED EVENTS ================= */}
      <div>
        <h2 className="text-2xl font-semibold text-green-700 mb-3">
          Saved Events
        </h2>

        {savedEvents.length === 0 ? (
          <p className="text-gray-500">You haven’t saved any events yet.</p>
        ) : (
          <div className="flex overflow-x-auto gap-4 pb-3">
            {savedEvents.map((event) => (
              <div
                key={event._id}
                className="min-w-[190px] h-[150px] bg-white border rounded-lg shadow-md p-4 relative flex flex-col justify-between"
              >
                {/* UNSAVE BUTTON */}
                <button
                  className="absolute top-2 right-2 text-xl hover:scale-110 transition"
                  onClick={() => unsaveEvent(event._id)}
                >
                  💚
                </button>

                <div>
                  <h3 className="font-semibold text-gray-800 text-md line-clamp-1">
                    {event.title}
                  </h3>
                  <p className="text-gray-500 text-sm mt-1">
                    {event.date || "No date"}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* ================= CREATED EVENTS (empty for now) ================= */}
      <div>
        <h2 className="text-2xl font-semibold text-green-700 mb-3">
          Created Events
        </h2>

        {createdEvents.length === 0 ? (
          <p className="text-gray-500">You haven’t created any events yet.</p>
        ) : (
          <div className="flex overflow-x-auto gap-4 pb-3">
            {createdEvents.map((event) => (
              <div
                key={event._id}
                className="min-w-[190px] h-[150px] bg-white border rounded-lg shadow-md p-4"
              >
                <h3 className="font-semibold text-gray-800 text-md line-clamp-1">
                  {event.title}
                </h3>
                <p className="text-gray-500 text-sm mt-1">
                  {event.date || "No date"}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* ================= LOGOUT ================= */}
      <button
        onClick={() => {
          localStorage.clear();
          navigate("/");
          window.location.reload();
        }}
        className="bg-red-600 text-white py-2 px-6 rounded-md hover:bg-red-700 text-lg w-fit"
      >
        Logout
      </button>
    </div>
  );
}
