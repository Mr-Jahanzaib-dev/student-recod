from ultralytics import YOLO
import cv2
cap = cv2.VideoCapture(r"utils\video.mp4")
model = YOLO(r"yolov8n\yolov8n.pt")
width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter(
    "results/output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            label = model.names[class_id]
            confidence = float(box.conf[0])
            cv2.rectangle(frame,
                          (x1, y1),
                          (x2, y2),
                          (0,200,0),
                          2)
            cv2.putText(frame,
                        f"{label} {confidence:.2f}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0,255,0),
                        2)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()