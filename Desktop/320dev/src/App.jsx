import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import MapView from "./pages/MapView";
import Account from "./pages/Account";

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/map" element={<MapView />} />
        <Route path="/account" element={<Account />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}
