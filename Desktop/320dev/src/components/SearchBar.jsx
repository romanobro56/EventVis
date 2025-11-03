// src/components/SearchBar.jsx
import { useState } from "react";
import useInView from "../hooks/useInView";

export default function SearchBar({ onSearch }) {
  const [ref, isVisible] = useInView({ threshold: 0.2 });
  const [query, setQuery] = useState("");
  const [filter, setFilter] = useState("Date");

  const handleSearch = () => {
    onSearch(query, filter);
  };

  return (
    <div
      ref={ref}
      className={`
        flex flex-wrap gap-3 p-4 bg-white/60 backdrop-blur rounded-lg shadow
        transform transition-all duration-700
        ${isVisible ? "opacity-100 translate-y-0" : "opacity-0 -translate-y-10"}
      `}
    >
      <input
        type="text"
        placeholder="Search events..."
        className="flex-1 px-3 py-2 rounded border border-gray-300"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSearch()}
      />
      <select
        className="px-3 py-2 rounded border border-gray-300"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      >
        <option>Date</option>
        <option>Price</option>
      </select>
      <button
        className="px-4 py-2 bg-green-700 text-white rounded hover:bg-green-800"
        onClick={handleSearch}
      >
        Search
      </button>
    </div>
  );
}
