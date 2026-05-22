from ultralytics import YOLO
import cv2
import math
import time

# ------------------------ Initialize Webcam ------------------------
cap = cv2.VideoCapture(0)
cap.set(3, 940)  # Width
cap.set(4, 780)  # Height

if not cap.isOpened():
    raise IOError("❌ Cannot open webcam")

# ------------------------ Load YOLO Model ------------------------
try:
    model = YOLO("yolo-Weights/yolov8n.pt")
except Exception as e:
    print(f"❌ Error loading YOLO model: {e}")
    exit()

# ------------------------ Use Model Class Names ------------------------
classNames = model.names  # Automatically load correct class labels

# ------------------------ Confidence Threshold ------------------------
CONFIDENCE_THRESHOLD = 0.5

# ------------------------ FPS Counter ------------------------
prev_time = 0

# ------------------------ Main Loop ------------------------
while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to read frame from webcam")
        break

    # Optional resize for performance
    # img = cv2.resize(img, (640, 480))

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            confidence = float(box.conf[0])
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])

            label = f"{classNames[cls] if cls in classNames else 'Unknown'} {confidence:.2f}"
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # ------------------------ Show FPS ------------------------
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time
    cv2.putText(img, f"FPS: {int(fps)}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # ------------------------ Display Frame ------------------------
    cv2.imshow("Webcam", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ------------------------ Cleanup ------------------------
cap.release()
cv2.destroyAllWindows()
