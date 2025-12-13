import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import MapView from "./pages/MapView";
import Account from "./pages/Account";
import Signup from "./pages/Signup";
import Profile from "./pages/Profile";
import { Toaster } from "react-hot-toast";
import EventCreation from "./pages/EventCreation";


export default function App() {
  const [user, setUser] = useState(null);

  return (
    <BrowserRouter>
      <Toaster position="top-center" />
      <Header user={user} setUser={setUser} />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/map" element={<MapView />} />
        <Route path="/account" element={<Account setUser={setUser} />} />
        <Route path="/signup" element={<Signup setUser={setUser} />} />

        {/* NEW: Profile Page */}
        <Route path="/profile" element={<Profile />} />

        <Route path="/create" element={<EventCreation />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}
