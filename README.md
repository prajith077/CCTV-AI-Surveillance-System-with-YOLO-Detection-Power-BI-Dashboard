# CCTV-AI-Surveillance-System-with-YOLO-Detection-Power-BI-Dashboar

The CCTV AI Surveillance System is a real-time video monitoring application that combines computer vision and web technologies to simulate intelligent security surveillance. This project uses the Ultralytics YOLOv8 model to detect people in video streams and highlights them with red bounding boxes, representing potential PPE (Personal Protective Equipment) violations. It is designed as a modular system with a FastAPI backend for video processing and streaming, and a modern Next.js frontend for visualization and user interaction.

The system supports multiple camera feeds by converting locally stored video files into live streams. Each stream is processed frame-by-frame using YOLO, and the annotated frames are delivered to the frontend via HTTP streaming. The frontend displays these streams in a responsive grid layout, allowing users to monitor multiple cameras simultaneously in real time.

In addition to live monitoring, the project integrates a Power BI dashboard to provide a separate analytics view. This dashboard can be embedded directly into the application and is intended to display insights such as detection counts, trends, or safety compliance metrics. While the current implementation uses simulated data, it demonstrates how AI-based detection systems can be connected with business intelligence tools.

The backend is built using FastAPI, OpenCV, and Ultralytics YOLOv8, ensuring efficient processing and scalability. The frontend is developed using Next.js with the App Router, providing a clean and professional user interface with navigation between the camera monitoring page and the dashboard page.

To run the project, the backend server must be started to serve the video streams, and the frontend application must be launched to display them in the browser. Once both are running, users can access the camera feeds from the main page and view the embedded Power BI dashboard on a separate route.

It is important to note that this project currently performs person detection only and does not implement true PPE detection such as helmet or safety vest recognition. However, it provides a strong foundation for extending into a full production-grade PPE compliance system.

This project can be further enhanced by adding real PPE detection models, integrating live data pipelines for dashboards, enabling alert systems, and supporting real IP camera streams via RTSP. It serves as a practical demonstration of how AI, backend services, and frontend dashboards can be combined into a unified surveillance solution.
