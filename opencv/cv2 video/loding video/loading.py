import cv2
cap = cv2.VideoCapture(r'C:\Users\User\Music\internship project\student recod\opencv\cv2 video\video\video.mp4')

if not cap.isOpened():
    print("Error: Could not open video file")
else:
    print("Video loaded successfully")