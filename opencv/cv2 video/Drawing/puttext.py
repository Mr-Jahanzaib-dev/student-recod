import cv2
cap = cv2.VideoCapture(r'C:\Users\User\Music\internship project\student recod\opencv\cv2 video\video\video.mp4')
if not cap.isOpened():
    print("Error: Could not open video file")
else:
    print("Video loaded successfully")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        cv2.putText(frame, "hello", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  
        cv2.imshow('Video Frame', frame)
        cv2.imwrite('output_video.mp4', frame) 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break  
    cap.release()
    cv2.destroyAllWindows()
