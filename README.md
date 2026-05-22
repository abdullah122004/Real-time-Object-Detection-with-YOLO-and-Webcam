# Real-time Object Detection with YOLO and Webcam

## 🔍 Introduction

Object detection is a critical task in computer vision, with numerous real-world applications ranging from surveillance to automation. This project implements a **real-time object detection system** using the **YOLO (You Only Look Once)** algorithm integrated with a webcam for live video streaming and detection.

## 🎯 Objectives

- Develop a real-time object detection system using YOLO.
- Integrate a webcam to process live video input.
- Detect and classify multiple objects in each video frame.
- Provide a lightweight and user-friendly detection system.


## 🛠 Methodology

1. **Environment Setup**  
   Install Python, OpenCV, and the Ultralytics YOLO library.
2. **Webcam Input**  
   Use OpenCV to capture live video stream from a webcam.
3. **YOLO Integration**  
   Load the YOLOv8 model for object detection.
4. **Frame Processing**  
   Analyze each frame, detect objects, and annotate them.
5. **Visualization**  
   Display detection results in real-time with bounding boxes and labels.
6. **Testing**  
   Verify detection accuracy and performance efficiency.

## 🧑‍💻 Implementation

### 1. Setting Up

- Install Python 3.8 or later
- Install required libraries: OpenCV and Ultralytics
- Download YOLOv8 pretrained weights (`yolov8n.pt`)

### 2. Code Flow

- Initialize the webcam.
- Load YOLO model and classes.
- Process and analyze each video frame in real time.
- Draw bounding boxes and labels for detected objects.
- Exit the loop gracefully when user presses `'q'`.

---

## ✅ Results

- Successfully detects and classifies multiple objects live.
- High frame rate and accuracy with efficient performance.
- Supports detection of common objects like persons, vehicles, bags, bottles, etc.
- Bounding boxes and class names shown in real-time on video stream.

---

## 📌 How to Install and Use

### 🔧 System Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Ultralytics (`ultralytics`)
- Webcam (internal or USB)
- GPU recommended for better performance

### 🚀 Installation Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/yolo-webcam-detection.git
   cd yolo-webcam-detection
   ---------------------------------------
(Optional) Create Virtual Environment

python -m venv yolo_env
# Activate:
source yolo_env/bin/activate       # Linux/macOS
yolo_env\Scripts\activate          # Windows
----------------------------
Install Required Packages

pip install opencv-python ultralytics

##Once you Run project Yolo weights will be downloaded Automatically

▶️ Run the Project

python main.py

The webcam will open and start real-time object detection.

Press q to exit.


📈 Future Work
🔁 Add multi-camera support

🧠 Improve detection accuracy using larger YOLO variants

🤖 Integrate AI-based logic for automated decisions

🍓 Deploy on edge devices like Raspberry Pi

🏭 Optimize for real-world, large-scale applications

