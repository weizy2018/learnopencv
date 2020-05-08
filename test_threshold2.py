import cv2 as cv 
import numpy as np 


# img = cv.imread("pic/sudoku.png", cv.IMREAD_GRAYSCALE)
img = cv.imread("pic/test.jpg", cv.IMREAD_GRAYSCALE)

dst = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 5)

cv.imshow("source", img)
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()