import cv2
cap = cv2.VideoCapture(r'C:\Users\User\Music\internship project\student recod\opencv\cv2 video\video\video.mp4')
if not cap.isOpened():
    print("Error: Could not open video file")
else:
    print("Video loaded successfully")
cap.set(cv2.CAP_PROP_POS_FRAMES,10)
ret, frame = cap.read()
if ret:
    cv2.imshow('Video Frame', frame)
    cv2.waitKey(0) 
cap.release()
cv2.destroyAllWindows()
