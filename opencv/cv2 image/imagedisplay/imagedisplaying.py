import cv2
img = cv2.imread(r'C:\Users\User\Music\internship project\student recod\opencv\image\python.jpg')
if img is  None :
    print("Image not found")
else:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

