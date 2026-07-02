import cv2
img = cv2.imread(r'C:\Users\User\Music\internship project\student recod\opencv\image\python.jpg')
if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    cv2.putText(img, "hello", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Image with Text', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()