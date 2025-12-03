const API_URL = "http://localhost:8000";

export async function fetchEvents() {
  const res = await fetch("http://localhost:8000/events");
  return res.json();
}

export async function fetchEventById(id) {
  const res = await fetch(`http://localhost:8000/events/${id}`);
  return res.json();
}

// can add more API calls here
