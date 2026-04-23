from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import os
from ultralytics import YOLO

app = FastAPI()

# ✅ CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEOS = {
    "cam1": os.path.join(BASE_DIR, "videos", "cam1.mp4"),
    "cam2": os.path.join(BASE_DIR, "videos", "cam2.mp4"),
    "cam3": os.path.join(BASE_DIR, "videos", "cam3.mp4"),
}

# ✅ YOLO model
model = YOLO("yolov8n.pt")


def generate(cam_id):
    path = VIDEOS.get(cam_id)

    print("📂 Path:", path)

    cap = cv2.VideoCapture(path)
    print("🎥 Opened:", cap.isOpened())

    if not cap.isOpened():
        return

    while True:
        success, frame = cap.read()

        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        results = model(frame, conf=0.4)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                if label == "person":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

        frame = cv2.resize(frame, (640, 360))
        _, buffer = cv2.imencode(".jpg", frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')


@app.get("/stream/{cam_id}")
def stream(cam_id: str):
    return StreamingResponse(
        generate(cam_id),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )