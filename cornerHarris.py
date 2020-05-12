import numpy as np 
import cv2 as cv 

# img = cv.imread("pic/blox.jpg", cv.IMREAD_COLOR)
img = cv.imread("pic/desk.jpg", cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.namedWindow("img", cv.WINDOW_NORMAL)
cv.imwrite("pic/desk1.jpg", img)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()