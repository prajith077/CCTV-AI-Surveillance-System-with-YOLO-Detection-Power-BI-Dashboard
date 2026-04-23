import "./globals.css";
import Link from "next/link";

export default function Layout({ children }: any) {
  return (
    <html>
      <body style={{ display: "flex" }}>
        
        <div className="sidebar">
          <h2>🚀 CCTV AI</h2>

          <Link href="/">
            <div className="menu">🎥 Cameras</div>
          </Link>

          <Link href="/dashboard">
            <div className="menu">📊 Dashboard</div>
          </Link>
        </div>

        <div className="main">{children}</div>
      </body>
    </html>
  );
}