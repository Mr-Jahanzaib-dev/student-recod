import cv2
cap = cv2.VideoCapture(r'C:\Users\User\Music\internship project\student recod\opencv\cv2 video\video\video.mp4')
if not cap.isOpened():
    print("Error: Could not open video file")
else:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))
    print("Video loaded successfully")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 255, 0), 2)  
        out.write(frame)
        cv2.imshow('Video Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break  
    cap.release()
    cv2.destroyAllWindows()
