import { useState } from "react";
import { MapContainer, TileLayer, Marker, useMapEvents } from "react-leaflet";

function LocationMarker({ onChange }) {
  const [position, setPosition] = useState(null);

  useMapEvents({
    click(e) {
      setPosition(e.latlng);
      onChange(e.latlng);
    }
  });

  return position ? <Marker position={position} /> : null;
}

export default function MapPicker({ onChange }) {
  return (
    <div>
      <MapContainer
        center={[42.3736, -72.5199]}
        zoom={13}
        style={{ height: "400px", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="© OpenStreetMap contributors"
        />
        <LocationMarker onChange={onChange} />
      </MapContainer>
    </div>
  );
}
