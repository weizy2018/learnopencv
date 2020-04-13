import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv.imread("pic/img_gray.png", cv.IMREAD_GRAYSCALE)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
plt.imshow(res, cmap='gray')
plt.show()