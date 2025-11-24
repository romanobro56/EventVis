const API_URL = "http://localhost:8000";

export async function fetchEvents() {
  const res = await fetch(`${API_URL}/events?search_text=temp`);
  const data = await res.json();
  return data;
}

// can add more API calls here
