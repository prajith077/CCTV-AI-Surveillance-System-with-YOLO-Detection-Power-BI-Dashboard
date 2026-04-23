"use client";

export default function Cameras() {
  const cams = ["cam1", "cam2", "cam3"];

  return (
    <div>
      <h1>🧠 YOLO Detection</h1>

      <div className="grid">
        {cams.map((cam) => (
          <div key={cam} className="card">
            <h3>{cam}</h3>

            <img
              src={`http://127.0.0.1:5000/stream/${cam}`}
              style={{ width: "100%", borderRadius: "10px" }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}