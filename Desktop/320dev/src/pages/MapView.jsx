import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const events = [
  { id: 1, title: "Farmers Market", lat: 42.3736, lng: -72.5199 },
  { id: 2, title: "Art Fair", lat: 42.376, lng: -72.52 },
];

export default function MapView() {
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
