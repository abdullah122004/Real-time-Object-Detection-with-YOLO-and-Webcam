# 📷 Real-time Object Detection with YOLO and Webcam

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black)

## 🔍 Introduction
Object detection is a critical task in computer vision, with numerous real-world applications ranging from surveillance to automation. This project implements a real-time object detection system using the highly efficient **YOLO (You Only Look Once)** algorithm, integrated seamlessly with a webcam for live video streaming and object classification.

---

## 🎯 Objectives
*   Develop a robust real-time object detection system using the YOLO architecture.
*   Integrate a webcam to capture and process live video inputs.
*   Detect, classify, and track multiple objects simultaneously within each video frame.
*   Provide a lightweight, user-friendly, and highly responsive detection system.

---

## 🛠 Methodology
1.  **Environment Setup:** Install Python, OpenCV, and the Ultralytics YOLO library.
2.  **Webcam Input:** Utilize OpenCV to capture a continuous live video stream from a hardware webcam.
3.  **YOLO Integration:** Load the pre-trained YOLOv8 model designed for high-speed object detection.
4.  **Frame Processing:** Analyze each frame dynamically, detect objects, and generate annotations.
5.  **Visualization:** Render the detection results in real-time, overlaying bounding boxes and class labels onto the video feed.
6.  **Testing:** Continuously verify detection accuracy, confidence scores, and processing performance (FPS).

---

## 🧑‍💻 Implementation Workflow

1.  **Setting Up:**
    *   Install Python 3.8 or later.
    *   Install required libraries: `OpenCV` and `Ultralytics`.
    *   Download YOLOv8 pre-trained weights (`yolov8n.pt`).
2.  **Code Flow:**
    *   Initialize the webcam hardware.
    *   Load the YOLO model and COCO dataset classes.
    *   Process and analyze each video frame in real-time.
    *   Draw bounding boxes and text labels for detected objects.
    *   Exit the processing loop gracefully when the user presses the `'q'` key.

---

## ✅ Results
*   Successfully detects and classifies multiple objects live with minimal latency.
*   Maintains a high frame rate (FPS) and accuracy, ensuring efficient hardware performance.
*   Supports the detection of 80+ common everyday objects (e.g., persons, vehicles, bags, bottles).
*   Dynamic bounding boxes and class names are rendered seamlessly in real-time on the video stream.

---

## 📌 How to Install and Use

### 🔧 System Requirements
*   **Python:** 3.8+
*   **Libraries:** `opencv-python`, `ultralytics`
*   **Hardware:** Internal built-in webcam or an external USB camera.
*   *Note: A dedicated GPU is recommended for maximum FPS, though standard CPUs will work perfectly for the lightweight `yolov8n` model.*
