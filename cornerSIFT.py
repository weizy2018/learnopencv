import numpy as np 
import cv2 as cv 

img = cv.imread("pic/desk.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
# img = cv.drawKeypoints(img, kp, img)
img = cv.drawKeypoints(img, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite("pic/sift.jpg", img)

cv.namedWindow("img", cv.WINDOW_NORMAL)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()