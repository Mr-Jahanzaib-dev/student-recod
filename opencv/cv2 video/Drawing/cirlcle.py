import cv2
import numpy as np
img = np.ones((400, 400, 3), dtype=np.uint8)
if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.circle(img, (50, 50), 50, (0, 255, 0), 3)
    cv2.imshow('Image with Rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()