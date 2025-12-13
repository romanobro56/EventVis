const API_URL = "http://localhost:8000";

export async function fetchEvents() {
  const res = await fetch(`${API_URL}/events`);
  return res.json();
}

export async function fetchEventById(id) {
  const res = await fetch(`${API_URL}/events/${id}`);
  return res.json();
}

export async function requestSignUp(name, email, password) {
  return await fetch(`${API_URL}/users/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, email, password }),
  });
}

export async function createEvent(eventData) {
  return await fetch(`${API_URL}/events`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(eventData),
  });
}

// can add more API calls here
