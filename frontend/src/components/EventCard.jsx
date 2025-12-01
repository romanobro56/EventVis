// src/components/EventCard.jsx
import { useState } from "react";
import useInView from "../hooks/useInView";
import CommentSection from "./CommentSection";

export default function EventCard({ event }) {
  const [ref, isVisible] = useInView({ threshold: 0.2 });
  const [expanded, setExpanded] = useState(false);
  const [liked, setLiked] = useState(false);

  return (
    <div
      ref={ref}
      className={`
        bg-white/80 rounded-2xl shadow-md hover:shadow-xl transition-all duration-700 p-5 cursor-pointer backdrop-blur-md
        transform transition-opacity duration-700
        ${isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"}
      `}
      onClick={() => setExpanded(!expanded)}
    >
      {/* Basic Info */}
      <div className="flex justify-between items-center">
        <h2 className="text-lg font-semibold text-green-900">{event.title}</h2>
        <button
          onClick={(e) => {
            e.stopPropagation(); // prevent card click toggle
            setLiked(!liked);
          }}
          className={`px-3 py-1 rounded ${
            liked ? "bg-red-500 text-white" : "bg-gray-200 text-gray-800"
          }`}
        >
          {liked ? "Liked ❤️" : "Like ♡"}
        </button>
      </div>
      <p className="text-gray-600">{event.date}</p>
      <p className="text-gray-700 mt-2">{event.description}</p>

      {/* Expanded Details */}
      {expanded && (
        <div className="mt-4 border-t border-gray-300 pt-4 space-y-2">
          <p className="text-gray-800">{event.full_description}</p>
          <p className="text-sm text-gray-600">
            <strong>Time:</strong> {event.start_time} - {event.end_time}
          </p>
          <p className="text-sm text-gray-600">
            <strong>Location:</strong> {event.location}
          </p>

          {/* Comment Section */}
          <CommentSection eventId={event.id} />
        </div>
      )}
    </div>
  );
}
