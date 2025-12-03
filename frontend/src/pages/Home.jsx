import { useEffect, useState } from "react";
import ParallaxBackground from "../components/ParallaxBackground";
import SearchBar from "../components/SearchBar";
import EventCard from "../components/EventCard";
import { fetchEvents } from "../api";
import toast from "react-hot-toast";

export default function Home() {
  const [events, setEvents] = useState([]);
  const [filteredEvents, setFilteredEvents] = useState([]);
  const [savedEvents, setSavedEvents] = useState(new Set());

  const API = "http://localhost:8000";

  // Load events + saved list
  useEffect(() => {
    const load = async () => {
      const data = await fetchEvents();
      setEvents(data);
      setFilteredEvents(data);

      const token = localStorage.getItem("token");

      if (token && token !== "null" && token !== "undefined") {
        const res = await fetch(`${API}/users/saved`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (res.ok) {
          const savedData = await res.json();
          const ids = savedData.saved_events.map((e) => e._id);
          setSavedEvents(new Set(ids));
        }
      }
    };

    load();
  }, []);

  // Save / Unsave
  const toggleSave = async (eventId) => {
    const token = localStorage.getItem("token");
    if (!token || token === "null" || token === "undefined") {
      toast.error("Please login to save events.");
      return;
    }

    const alreadySaved = savedEvents.has(eventId);
    const url = alreadySaved
      ? `${API}/events/${eventId}/unsave`
      : `${API}/events/${eventId}/save`;

    const res = await fetch(url, {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });

    if (res.ok) {
      setSavedEvents((prev) => {
        const updated = new Set(prev);
        if (alreadySaved) updated.delete(eventId);
        else updated.add(eventId);
        return updated;
      });
    }
  };

  // Search
  const handleSearch = (query) => {
    const lower = query.toLowerCase();
    setFilteredEvents(events.filter((e) => e.title.toLowerCase().includes(lower)));
  };

  return (
    <div className="min-h-screen relative">
      <ParallaxBackground />

      <div className="max-w-4xl mx-auto p-6 space-y-8 relative z-10">
        <SearchBar onSearch={handleSearch} />

        <div className="grid grid-cols-1 gap-6">
          {filteredEvents.length > 0 ? (
            filteredEvents.map((event) => (
              <EventCard
                key={event._id}
                event={event}
                savedEvents={savedEvents}
                toggleSave={toggleSave}
              />
            ))
          ) : (
            <p className="text-gray-600 text-center">No events found.</p>
          )}
        </div>
      </div>
    </div>
  );
}
