import { useState } from "react";
import { useNavigate } from "react-router-dom";
import MapPicker from "../components/MapPicker";
import { createEvent } from "../api";

export default function EventCreation() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    full_description: "",
    date: "",
    start_time: "",
    end_time: "",
    location: "",
    lat: "",
    lng: "",
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(formData);
    const res = await createEvent(formData);
    navigate("/");
  };
  

  return (
    <div className="max-w-md mx-auto p-8">
      <h2 className="text-3xl font-bold text-green-800 mb-6">Create Event</h2>

      {error && (
        <p className="bg-red-200 text-red-800 p-2 rounded mb-4">{error}</p>
      )}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-gray-700 font-medium">Title</label>
          <input
            type="text"
            name="title"
            className="w-full p-2 border rounded mt-1"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Description</label>
          <input
            type="text"
            name="description"
            className="w-full p-2 border rounded mt-1"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Full Description</label>
          <input
            type="text"
            name="full_description"
            className="w-full p-2 border rounded mt-1"
            value={formData.full_description}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Date</label>
          <input
            type="date"
            name="date"
            className="w-full p-2 border rounded mt-1"
            value={formData.date}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Start Time</label>
          <input
            type="time"
            name="start_time"
            className="w-full p-2 border rounded mt-1"
            value={formData.start_time}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">End Time</label>
          <input
            type="time"
            name="end_time"
            className="w-full p-2 border rounded mt-1"
            value={formData.end_time}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Location Name</label>
          <input
            type="text"
            name="location"
            className="w-full p-2 border rounded mt-1"
            value={formData.location}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label className="block text-gray-700 font-medium">Location</label>
          <MapPicker
            onChange={coords => {
              setFormData(prev => ({
                ...prev,
                lat: coords.lat,
                lng: coords.lng,
              }));
            }}
          />
        </div>

        <button
          type="submit"
          className="w-full bg-green-700 text-white py-2 rounded hover:bg-green-800"
        >
          Create
        </button>
      </form>
    </div>
  );
}
