import { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { fetchEvents } from "../api";

export default function MapView() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    (async () => {
      const data = await fetchEvents();
      setEvents(data);
    })();
  }, []);

  return (
    <div className="h-screen w-full">
      <MapContainer center={[42.3736, -72.5199]} zoom={13} className="h-full w-full z-0">
        <TileLayer
          attribution='&copy; <a href="http://osm.org">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {events.map((e) => (
          <Marker key={e.id} position={[e.lat, e.lng]}>
            <Popup>{e.title}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
