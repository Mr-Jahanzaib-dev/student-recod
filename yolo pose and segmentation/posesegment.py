import cv2
from ultralytics import YOLO

pose_model = YOLO("yolo11n-pose.pt")
seg_model = YOLO("yolo11n-seg.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
        
    
    seg_results = seg_model(frame, stream=True, verbose=False)
    for r in seg_results:
        frame = r.plot()  
        
    
    pose_results = pose_model(frame, stream=True, verbose=False)
    for r in pose_results:
        frame = r.plot()  
    
    cv2.imshow("Pose + Instance Segmentation Tracker", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()