import { useEffect, useState } from "react";

export default function ParallaxBackground() {
  const [scroll, setScroll] = useState(0);

  useEffect(() => {
    const onScroll = () => setScroll(window.scrollY);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // Calculate gradient position based on scroll
  const scrollPercent = Math.min(scroll / (document.body.scrollHeight - window.innerHeight), 1);
  const colorStop = scrollPercent * 100;

  return (
    <div
      className="fixed inset-0 -z-10 transition-all duration-300"
      style={{
        background: `linear-gradient(to bottom, #69940A ${colorStop}%, white 100%)`,
      }}
    />
  );
}
