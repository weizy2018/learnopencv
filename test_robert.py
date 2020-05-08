import cv2 as cv 
import numpy as np 

def robert(img_gray):
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = cv.filter2D(img_gray, cv.CV_16S, kernelx)
    y = cv.filter2D(img_gray, cv.CV_16S, kernely)

    absX = cv.convertScaleAbs(x)
    absy = cv.convertScaleAbs(y)
    
    dst = cv.addWeighted(absX, 0.5, absy, 0.5, 0)
    return dst

img = cv.imread("pic/lena.jpg", cv.IMREAD_GRAYSCALE)
dst = robert(img)
cv.imshow("robert", dst)
cv.waitKey(0)
cv.destroyAllWindows()