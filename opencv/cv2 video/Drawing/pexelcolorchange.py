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
        frame[100:150, 100:150] = [0, 0, 255]  
        cv2.imshow('Video Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break  
    cap.release()
    cv2.destroyAllWindows()
