import numpy as np 
import cv2 as cv 

image = cv.imread("pic1.jpg", cv.IMREAD_COLOR)
se = cv.getStructuringElement(cv.MORPH_DILATE, (5, 5))
print(se)
image2 = cv.morphologyEx(image, cv.MORPH_DILATE, se)

cv.namedWindow("source", cv.WINDOW_NORMAL)
cv.namedWindow("image2", cv.WINDOW_NORMAL)

cv.imshow("source", image)
cv.imshow("image2", image2)
cv.waitKey()
cv.destroyAllWindows()