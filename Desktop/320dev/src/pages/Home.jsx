import { useState } from "react";
import ParallaxBackground from "../components/ParallaxBackground";
import SearchBar from "../components/SearchBar";
import EventCard from "../components/EventCard";

// Dummy event data
const dummyEvents = [
  {
    event_id: 1,
    title: "Farmers Market",
    date: "Nov 10",
    description: "Local produce and crafts",
    fullDescription: "Come enjoy fresh local produce, crafts, and music at the farmers market!",
    start_time: "09:00",
    end_time: "15:00",
    location: "Central Park",
  },
  {
    event_id: 2,
    title: "Art in the Park",
    date: "Nov 12",
    description: "Outdoor art showcase",
    fullDescription: "Experience local artists showcasing their work in a beautiful outdoor setting.",
    start_time: "11:00",
    end_time: "17:00",
    location: "Riverside Park",
  },
  {
    event_id: 3,
    title: "Food Festival",
    date: "Nov 15",
    description: "Tasty eats and live music",
    fullDescription: "Sample cuisines from around the world while enjoying live performances.",
    start_time: "12:00",
    end_time: "20:00",
    location: "Downtown Square",
  },
];

export default function Home() {
  const [events] = useState(dummyEvents);
  const [filteredEvents, setFilteredEvents] = useState(events);

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
              <EventCard key={event.event_id} event={event} />
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
