import numpy as np 
import cv2 as cv 

img = cv.imread("pic/blox.jpg", cv.IMREAD_GRAYSCALE)
surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img, None)
print(len(kp))
print(surf.getHessianThreshold())
surf.setHessianThreshold(600)
kp, des = surf.detectAndCompute(img, None)
print(len(kp))
img = cv.drawKeypoints(img, kp, img)
cv.namedWindow("img", cv.WINDOW_NORMAL)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()