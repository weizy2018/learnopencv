import cv2 as cv 
import numpy as np 

img = cv.imread("WindowsLogo.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
img = cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.namedWindow("key points", cv.WINDOW_NORMAL)
cv.imshow("key points", img)
cv.waitKey(0)
cv.destroyAllWindows()