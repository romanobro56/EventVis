import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import MapView from "./pages/MapView";
import Account from "./pages/Account";
import Signup from "./pages/Signup";

export default function App() {
  const [user, setUser] = useState(null);

  return (
    <BrowserRouter>
      <Header user={user} />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/map" element={<MapView />} />

        {/* Login */}
        <Route path="/account" element={<Account setUser={setUser} />} />

        {/* Signup */}
        <Route path="/signup" element={<Signup setUser={setUser} />} />
      </Routes>

      <Footer />
    </BrowserRouter>
  );
}
