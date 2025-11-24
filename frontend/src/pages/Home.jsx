import { useEffect, useState } from "react";
import ParallaxBackground from "../components/ParallaxBackground";
import SearchBar from "../components/SearchBar";
import EventCard from "../components/EventCard";
import { fetchEvents } from "../api";

export default function Home() {
  const [events, setEvents] = useState([]);
  const [filteredEvents, setFilteredEvents] = useState(events);

  useEffect(() => {
    (async () => {
      const data = await fetchEvents();
      setEvents(data);
      setFilteredEvents(data);
    })();
  }, []);

  // Frontend search
  const handleSearch = (query, filter) => {
    const lower = query.toLowerCase();
    setFilteredEvents(
      events.filter((e) => e.title.toLowerCase().includes(lower))
    );
  };

  return (
    <div className="min-h-screen relative">
      <ParallaxBackground />

      <div className="max-w-4xl mx-auto p-6 space-y-8 relative z-10">
        <SearchBar onSearch={handleSearch} />

        <div className="grid sm:grid-cols-2 gap-6">
          {filteredEvents.length > 0 ? (
            filteredEvents.map((event) => (
              <EventCard key={event.id} event={event} />
            ))
          ) : (
            <p className="text-gray-600 col-span-full text-center">
              No events found.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
