import { useState } from "react";

export default function EventCard({ event, savedEvents, toggleSave }) {
  const [expanded, setExpanded] = useState(false);

  const isSaved = savedEvents.has(event._id);

  return (
    <div
      className="p-4 bg-white rounded shadow transition cursor-pointer"
      onClick={() => setExpanded(!expanded)}
    >
      <div className="flex justify-between items-center">
        <h3 className="text-xl font-bold">{event.title}</h3>

        <button
          className="flex items-center gap-1 px-2 py-1 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-100"
          onClick={(e) => {
            e.stopPropagation();
            toggleSave(event._id);
          }}
        >
          {isSaved ? "💚 Saved" : "🤍 Save"}
        </button>
      </div>

      <p className="text-gray-600">{event.date}</p>
      <p>{event.description}</p>

      {expanded && (
        <div className="mt-4 text-gray-700">
          <p><strong>Time:</strong> {event.start_time} – {event.end_time}</p>
          <p><strong>Location:</strong> {event.location}</p>
          <p className="mt-2">{event.full_description}</p>
        </div>
      )}
    </div>
  );
}
