// src/components/Header.jsx
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";

export default function Header({ user, setUser }) {
  const location = useLocation();
  const navigate = useNavigate();
  const [menuOpen, setMenuOpen] = useState(false);

  const logout = () => {
    localStorage.clear();
    setUser(null);
    navigate("/");
  };

  return (
    <header className="p-4 bg-green-700 text-white flex justify-between items-center">
      <h1 className="text-xl font-bold">EventVis</h1>

      <nav className="flex gap-6 items-center">

        {/* Main navigation links */}
        {location.pathname !== "/" && <Link to="/">Home</Link>}
        {location.pathname !== "/map" && <Link to="/map">Map</Link>}

        {/* NOT LOGGED IN → Show Login (but not on login page itself) */}
        {!user && location.pathname !== "/account" && (
          <Link to="/account">Login</Link>
        )}

        {/* LOGGED IN → PROFILE DROPDOWN */}
        {user && (
          <div
            className="relative inline-block"
            onMouseEnter={() => setMenuOpen(true)}
            onMouseLeave={() => setMenuOpen(false)}
          >
            <button className="bg-white text-green-700 px-4 py-2 rounded-md shadow hover:bg-gray-100 transition">
              My Profile
            </button>

            {menuOpen && (
              <div
                className="
                  absolute right-0 top-full
                  bg-white text-black w-44
                  rounded-md shadow-lg border border-gray-200
                  z-50
                "
              >
                <button
                  className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  onClick={() => navigate("/profile")}
                >
                  My Profile
                </button>

                <button
                  className="block w-full text-left px-4 py-2 hover:bg-gray-100"
                  onClick={logout}
                >
                  Logout
                </button>
              </div>
            )}
          </div>
        )}
      </nav>
    </header>
  );
}
