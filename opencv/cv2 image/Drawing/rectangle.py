import cv2
import numpy as np
img = cv2.imread(r'C:\Users\User\Music\internship project\student recod\opencv\image\python.jpg')
if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)
    cv2.imshow('Image with Rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r'C:\Users\User\Music\internship project\student recod\opencv\image\python_with_rectangle.jpg', img)