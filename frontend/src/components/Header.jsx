import { Link, useLocation } from "react-router-dom";

export default function Header({ user }) {
  const location = useLocation();

  return (
    <header className="p-4 bg-green-700 text-white flex justify-between items-center">
      <h1 className="text-xl font-bold">EventVis</h1>

      <nav className="flex gap-4">

        {/* Hide Home link when already on Home */}
        {location.pathname !== "/" && <Link to="/">Home</Link>}

        {/* Hide Map link when already on Map */}
        {location.pathname !== "/map" && <Link to="/map">Map</Link>}

        {!user ? (
          <>
            {/* Only show Login if not already on Login page */}
            {location.pathname !== "/account" && <Link to="/account">Login</Link>}

            {/* 🚫 NEVER show Sign Up link — removed permanently */}

          </>
        ) : (
          <>
            <span>Welcome, {user.name}!</span>
            <button
              onClick={() => {
                localStorage.clear();
                window.location.reload();
              }}
              className="bg-white text-green-700 px-3 py-1 rounded"
            >
              Logout
            </button>
          </>
        )}
      </nav>
    </header>
  );
}
