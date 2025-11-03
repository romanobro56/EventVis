import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="bg-white/70 backdrop-blur-md shadow-md p-4 flex justify-between items-center sticky top-0 z-50">
      <h1 className="text-2xl font-bold text-green-800">EventFinder</h1>
      <nav className="space-x-6">
        <Link to="/" className="hover:text-green-700">Home</Link>
        <Link to="/map" className="hover:text-green-700">Map</Link>
        <Link to="/account" className="hover:text-green-700">Account</Link>
      </nav>
    </header>
  );
}
