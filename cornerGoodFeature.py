import cv2 as cv 
import numpy as np 

img = cv.imread("pic/desk.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,45,0.01,10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, (0, 0, 255), -1)

cv.imwrite("pic/desk2.jpg", img)
cv.imshow("dst", img)
cv.waitKey(0)
